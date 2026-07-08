"""Option A — CNN from scratch (PyTorch).

À compléter si votre binôme choisit l'option A.
Architecture suggérée : 3-5 conv layers + 2 dense.
"""
from __future__ import annotations

import torch
import torch.nn as nn

from src.load_data import CLASSES


class SimpleCNN(nn.Module):
    """CNN simple from scratch pour PCB defect detection.

    Input : (B, 1, 64, 64) niveaux de gris.
    Output : (B, len(CLASSES)) logits.
    """

    def __init__(self, n_classes: int = len(CLASSES)):
        super().__init__()
        # Bloc extracteur de features : on transforme progressivement l'image brute
        # (1 canal, 64x64) en représentations plus riches et plus compactes.
        self.features = nn.Sequential(
            # Bloc 1 : détecte des motifs simples (bords, petites textures).
            nn.Conv2d(1, 16, kernel_size=3, padding=1),
            nn.BatchNorm2d(16),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2),  # 64 -> 32
            # Bloc 2 : combine les motifs du bloc 1 en structures plus complexes.
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2),  # 32 -> 16
            # Bloc 3 : niveau de représentation plus abstrait utile à la classification.
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2),  # 16 -> 8
        )

        # Tête de classification : convertit les features 2D en logits de classes.
        self.classifier = nn.Sequential(
            # (B, 64, 8, 8) -> (B, 4096)
            nn.Flatten(),
            # Couche dense intermédiaire pour apprendre des combinaisons globales.
            nn.Linear(64 * 8 * 8, 128),
            nn.ReLU(inplace=True),
            # Régularisation pour limiter l'overfitting.
            nn.Dropout(p=0.3),
            # Logits finaux : une valeur par classe PCB.
            nn.Linear(128, n_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # 1) Extraction de caractéristiques visuelles.
        x = self.features(x)
        # 2) Projection en logits pour CrossEntropyLoss.
        return self.classifier(x)


def train_one_epoch(model, loader, optimizer, criterion, device):
    """Boucle d'entraînement d'1 epoch."""
    # Active le mode entraînement (BatchNorm/Dropout se comportent en mode train).
    model.train()
    # Accumulateurs pour calculer les métriques moyennes sur tout le dataset.
    total_loss = 0.0
    correct = 0
    total = 0

    # Une epoch = un passage complet sur tous les mini-batches du loader train.
    for X, y in loader:
        # Déplace batch et labels sur CPU/GPU selon `device`.
        X, y = X.to(device), y.to(device)

        # Remet les gradients à zéro avant le backward du batch courant.
        optimizer.zero_grad()

        # Forward pass : logits prédits par le réseau.
        logits = model(X)
        # Calcule la loss de classification (CrossEntropy en général ici).
        loss = criterion(logits, y)

        # Backpropagation : calcule dL/dw pour tous les paramètres.
        loss.backward()
        # Mise à jour des poids selon l'optimiseur (Adam/SGD...).
        optimizer.step()

        # Cumule la loss pondérée par la taille du batch pour une moyenne correcte.
        total_loss += loss.item() * X.size(0)
        # Classe prédite = argmax des logits.
        preds = logits.argmax(dim=1)
        # Compte les bonnes prédictions pour l'accuracy.
        correct += (preds == y).sum().item()
        total += X.size(0)

    # Retourne les métriques moyennes sur l'epoch complète.
    return total_loss / total, correct / total


def evaluate(model, loader, criterion, device):
    """Évaluation sur un loader (val ou test)."""
    # Active le mode évaluation (désactive notamment le Dropout).
    model.eval()
    total_loss = 0.0
    correct = 0
    total = 0

    # Pas de calcul de gradients : plus rapide et moins de mémoire en évaluation.
    with torch.no_grad():
        for X, y in loader:
            # Déplace batch et labels sur CPU/GPU selon `device`.
            X, y = X.to(device), y.to(device)

            # Forward uniquement (pas de backward, pas d'update des poids).
            logits = model(X)
            loss = criterion(logits, y)

            # Même logique d'agrégation que pour le train, pour obtenir des moyennes globales.
            total_loss += loss.item() * X.size(0)
            preds = logits.argmax(dim=1)
            correct += (preds == y).sum().item()
            total += X.size(0)

    # Retourne la loss moyenne et l'accuracy sur l'ensemble évalué.
    return total_loss / total, correct / total
