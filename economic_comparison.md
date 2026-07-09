# Comparatif économique 3 approches — PCB Defect

> Document remis à **Inès Tabet** (Mistral) qui relaie à **TechniMatic**.
> Auteurs : `Théo` × `Romain` — Date : `09/07/2026`

## Méthodologie

- **Options A et B implémentées** : mesures **réelles** sur train + inférence
- **Option C non implémentée** : estimation argumentée via sources
  publiques (mini-cours + documentation CLIP)
- ⚠️ **Ordres de grandeur uniquement** : latence, temps d'entraînement et coût
  dépendent fortement du **hardware** (CPU/GPU, RAM, machine). On compare des
  **échelles relatives**, pas des vérités absolues.

Hypothèses communes pour la comparaison :
- Données disponibles : ~2100 images au total (train ~1500)
- Matériel de mesure : CPU local (pas de GPU dédié)
- Coût cloud : non retenu ici (expériences exécutées en local)

## Tableau

| Critère | Option A (CNN scratch) | Option B (Transfer ResNet-18) | Option C (Zero-shot CLIP) |
|---|---|---|---|
| **Statut** | **Mesuré** | **Mesuré** (V2 retenue, V1 baseline) | **Estimé** |
| **Données d'entraînement requises** | ~1500 (train) | ~1500 (train) | **0** |
| **Temps train (CPU)** | **56.57 s** (10 epochs) | **491.81 s** (V2, 10 epochs) | **0 s** (pas d'entraînement) |
| **Latence inférence / image (CPU)** | **1.519 ms** | **35.165 ms** (V2) | **~80-200 ms** (estimé) |
| **Mémoire modèle (Mo)** | **~2.0 Mo** (`cnn_romain.joblib`) | **~44.8 Mo** (`option_b_resnet18_v2_layer4_fc.pth`) | **~150 Mo** (poids téléchargés) |
| **Accuracy attendue** | **0.7556** (mesuré test) | **0.7905** (mesuré test V2) | **faible à moyenne** sur PCB spécifique (estimé ~20-50%) |
| **Coût € (training cloud)** | ~$0 (CPU local) | ~$0 (CPU local) | $0 |
| **Coût € (API)** | $0 (modèle local) | $0 (modèle local) | $0 (modèle local) |
| **Maintenance** | Réentraîner régulièrement (pipeline simple) | Réentraîner régulièrement (fine-tuning + suivi overfit) | Pas de réentraînement, mais prompts à maintenir/affiner |

**Légende** :
- **Mesuré** : valeur obtenue dans notre implémentation
- **Estimé** : valeur extrapolée de sources publiques (citer)

Notes :
- Option B V1 (backbone gelé) : 185.78 s, acc 0.5079, latence 32.808 ms.
- Option B V2 (layer4 + fc) : 491.81 s, acc 0.7905, latence 35.165 ms.
- Le gain de précision de V2 (+0.2826) justifie le surcoût de temps train.

## Sources des estimations

> Pour l'option non implémentée, cite tes sources.

- Estimation Option C :
  - HuggingFace CLIP docs : <https://huggingface.co/docs/transformers/model_doc/clip>
  - Model card `openai/clip-vit-base-patch32` : <https://huggingface.co/openai/clip-vit-base-patch32>
  - Référence interne : `ressources/03_Zero_shot_CLIP_essentiel.md` (latence CPU ~80-200 ms, performances variables sur classes spécifiques PCB)

## Comparaison qualitative

| Aspect | Option A | Option B | Option C |
|---|---|---|---|
| **Quand préférer** | Budget latence très strict, modèle léger, déploiement edge/CPU | Objectif de précision élevé avec données labellisées disponibles | MVP immédiat sans labels, exploration rapide |
| **Quand éviter** | Si on vise la meilleure précision sur défauts subtils | Si budget calcul/temps train très contraint | Si exigence qualité élevée sur classes PCB spécialisées |
| **Domaine adapté** | Cas simples à intermédiaires, contraintes temps réel fortes | Cas industriels de classification visuelle avec compromis coût/perf | Cas génériques ou prototypage, moins adapté au PCB ici |

## Synthèse

- **Option recommandée dans ce contexte** : **Option B V2**, meilleur score de précision (0.7905) pour une latence encore compatible (35.165 ms CPU).
- **Alternative coût/latence** : **Option A**, très rapide en inférence (1.519 ms) et très légère (~2 Mo), avec une précision légèrement inférieure.
- **Option C** : utile en baseline sans labels, mais risque de sous-performance sur défauts PCB spécialisés.

---

*Comparatif produit en binôme — `09/07/2026`.*
