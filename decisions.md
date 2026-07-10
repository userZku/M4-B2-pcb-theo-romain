# Décisions du binôme — M4-B2 (PCB Defect)

> À compléter à 2 dès la coordination kick-off jeudi matin.
> Servira de référence en RDV vendredi + restitution duo mardi 1ᵉʳ sept (rentrée M5).

## 1. Option choisie pour l'implémentation

> Une seule option implémentée jusqu'à l'inférence. Les 2 autres sont
> estimées (mini-prototypes + sources publiques).

**Choix** : ☐ Option A (CNN scratch) ☑ Option B (Transfer learning) ☐ Option C (Zero-shot CLIP)

**Argument** :
- D'après la grille de décision, étant donné qu'on a de la donnée labélisé en pas très grande quantité on élimine l'option C, que l'on peut garder en BaseLine car rapide à mettre en place.
- On n'a pas énormément de donnée donc la meilleur option dans les options qui reste est l'option B
- L'option A reste aussi un baseline intéressante mais moins adaptée que l'option B

## 2. Répartition des tâches binôme

| Tâche | Membre 1 (`Théo`) | Membre 2 (`Romain`) | Modalité |
|---|---|---|---|
| Setup repo + EDA | ☑ | ☑ | pair-coding |
| Implémentation option | Option B | Option A | MP |
| Comparatif économique | ☑ | ☑ | MP |
| README + restitution | ☑ | ☑ | MP |

## 3. Coordination Discord

- **Matin** (~9h) : check-in MP — qui fait quoi aujourd'hui ?
- **Midi** : point d'étape — qu'est-ce qui est mergé ?
- **Soir** : ce qui reste pour demain
- **Vendredi 11h** : test croisé du repo (chacun clone et teste le code de l'autre)

## 4. Git

- `main` seulement avec des prénoms
- `merge` quand au fur et à mesure

## 5. Restitution duo mardi 1ᵉʳ sept (rentrée M5)

- **Membre 1 (`Théo`)** présente : l'EDA, l'option B (transfer learning), les résultats V1/V2 et la démonstration technique.
- **Membre 2 (`Romain`)** présente : l'option A (CNN), la comparaison économique et l'argumentation finale.
- 5 min total + 5 min discussion

## 6. Points négociés (à expliciter en cas de désaccord)

> Si vous n'êtes pas d'accord sur un choix, tracez-le honnêtement ici.

- Option B retenue comme recommandation finale car meilleure précision mesurée sur le test standard.
- Option A conservée comme baseline solide car plus légère et plus rapide en entraînement et en inférence.
- Le notebook commun est limité à l'EDA et à la comparaison, les implémentations détaillées restent séparées dans les notebooks individuels.

---

*Décisions tracées par le binôme `Théo` × `Romain` — `08/07/2026`.*
