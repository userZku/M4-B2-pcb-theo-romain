# Verdict — Recommandation TechniMatic via Mistral

> 8 lignes maximum.
> Auteurs : `Théo` × `romain` — Date : `09/07/2026`

**Recommandation** : déployer l'Option B (Transfer learning ResNet-18, version V2 layer4 + fc).

**Raison principale (chiffrée)** : meilleure précision mesurée sur test (0.7905) avec une latence CPU encore compatible (35.165 ms/image), devant l'Option A (0.7556 ; 1.519 ms) et au-dessus de l'Option C estimée plus faible sur des classes PCB spécifiques.

**Condition de changement d'avis** : si la contrainte de latence devient prioritaire (inférence ultra-rapide en edge/CPU faible), alors je proposerais l'Option A. Si aucune donnée labellisée n'est disponible au démarrage, alors je proposerais l'Option C comme baseline MVP.

---

*Verdict binôme — `09/07/2026`.*
