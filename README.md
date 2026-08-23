# 🛡️ Alarme Manager Community

**Alarme Manager Community** est une intégration personnalisée pour **Home Assistant** qui ajoute une couche de supervision et d'orchestration autour d'une centrale existante, notamment **Alarmo**.

> **Beta communautaire ouverte aux tests.** Le moteur démarre en **OBSERVATION**. Les réactions physiques automatiques sont désactivées par défaut et doivent être autorisées explicitement.

## 🚀 Télécharger et essayer maintenant

### Option 1 — HACS (recommandé)

1. Ouvrez **HACS → Intégrations**.
2. Ajoutez `https://github.com/cybersquatbis/home-assistant-alarm-manager` comme **dépôt personnalisé** de catégorie **Integration**.
3. Recherchez **Alarme Manager Community** et installez-le.
4. Redémarrez Home Assistant.
5. Ouvrez **Paramètres → Appareils et services → Ajouter une intégration**.
6. Recherchez **Alarme Manager Community**.
7. Configurez votre centrale / Alarmo et les équipements à superviser.
8. Gardez le mode **OBSERVATION** pour les premiers essais.

### Option 2 — téléchargement ZIP

Téléchargez directement la branche `main` :

**https://github.com/cybersquatbis/home-assistant-alarm-manager/archive/refs/heads/main.zip**

Décompressez l'archive puis copiez :

`custom_components/alarme_manager/`

vers :

`/config/custom_components/alarme_manager/`

Redémarrez ensuite Home Assistant et ajoutez l'intégration depuis **Paramètres → Appareils et services**.

### Tester sans risque

Au premier démarrage :

- laissez **OBSERVATION** activé ;
- configurez d'abord la centrale et les capteurs ;
- utilisez `alarme_manager.simulate_incident` pour tester le comportement sans sortie physique ;
- testez séparément les lumières et la sirène avec confirmation explicite ;
- n'activez le mode ACTIF qu'après validation de votre configuration.

👉 **Les retours et rapports de bugs sont les bienvenus dans les Issues GitHub.** Merci d'indiquer la version Home Assistant, la version d'Alarme Manager et les logs utiles en retirant les informations sensibles.

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
