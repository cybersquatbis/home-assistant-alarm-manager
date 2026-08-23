# 🛡️ Alarme Manager Community

**Alarme Manager Community** est une intégration personnalisée pour **Home Assistant** qui ajoute une couche de supervision et d'orchestration autour d'une centrale existante, notamment **Alarmo**.

> **Beta communautaire.** Le moteur démarre en **OBSERVATION**. Les réactions physiques automatiques sont désactivées par défaut et doivent être autorisées explicitement.

## Alarmo ou Alarme Manager ?

**Alarmo reste la centrale** : armement, désarmement, modes, capteurs et déclenchement.

**Alarme Manager est la couche de supervision** : plan maison, contexte d'incident, santé des équipements, RF, historique, notifications et orchestration protégée des caméras, lumières et sirène.

Les deux sont complémentaires.

## Beta actuelle

- panneau latéral Home Assistant et plan maison générique ;
- ouvrants, mouvements, caméras, lumières, sirène, RF et équipements critiques configurables ;
- OBSERVATION par défaut et passage ACTIF avec confirmation ;
- historique local des 100 derniers incidents ;
- score de protection et détection des entités indisponibles ;
- surveillance RF / anti-brouillage basée sur les entités choisies ;
- simulation d'incident sans sortie physique ;
- tests manuels courts et confirmés ;
- captures caméra, notifications, lumières et sirène optionnelles lors d'une alarme ;
- profils `notify.*` stockables par le backend ;
- garde interne contre deux traitements de réaction simultanés ;
- sélection d'un capteur pluie prévue pour les futures règles ouvrants/Velux ;
- traductions FR/EN de la configuration.

## Installation manuelle

1. Copiez `custom_components/alarme_manager/` dans `/config/custom_components/alarme_manager/`.
2. Redémarrez Home Assistant.
3. Ouvrez **Paramètres → Appareils et services → Ajouter une intégration**.
4. Recherchez **Alarme Manager Community**.
5. Sélectionnez votre centrale / Alarmo et les équipements à superviser.
6. Ouvrez **Alarme Manager** dans la barre latérale.
7. Restez en **OBSERVATION** tant que les tests ne sont pas terminés.

## HACS

Le dépôt contient `hacs.json`. Tant qu'il n'est pas référencé dans le catalogue HACS par défaut, ajoutez-le comme **dépôt personnalisé de type Integration**.

## Sécurité par défaut

- OBSERVATION est la valeur initiale persistante ;
- lumières et sirène automatiques sont désactivées par défaut ;
- le passage en ACTIF exige `confirm: true` ;
- les tests physiques exigent `confirm: true` et sont limités à 10 secondes ;
- une simulation ne commande jamais de sortie ;
- aucune entité, aucun téléphone et aucun plan personnel ne sont fournis.

## Services

`alarme_manager.set_mode`, `alarme_manager.simulate_incident`, `alarme_manager.clear_history` et `alarme_manager.test_output`.

## Limites connues

Cette beta est une base Community fonctionnelle, pas un système d'alarme certifié. Restent à enrichir : corrélation avancée par zone, profils photo par téléphone, règles météo ouvrants/Velux, détection des doublons avec les automatisations externes et intégration RFPlayer dédiée.

## Documentation

[Installation](docs/INSTALLATION.md) · [Sécurité](docs/SECURITY.md) · [Confidentialité](docs/PRIVACY.md) · [Architecture](docs/ARCHITECTURE.md) · [Changelog](CHANGELOG.md)

## Licence

MIT — voir [LICENSE](LICENSE).
