# 🛡️ Alarme Manager Community

**Alarme Manager Community** est une intégration personnalisée pour **Home Assistant** qui ajoute une couche de supervision et d'orchestration autour d'une centrale existante, notamment **Alarmo**.

> **Beta communautaire ouverte aux tests — 0.2.0-beta.1.** Le moteur démarre en **OBSERVATION**. Les réactions physiques automatiques sont désactivées par défaut et doivent être autorisées explicitement.

## 🚀 Télécharger et essayer maintenant

### Option 1 — HACS (recommandé)

1. Ouvrez **HACS → Intégrations**.
2. Ajoutez `https://github.com/cybersquatbis/home-assistant-alarm-manager` comme **dépôt personnalisé** de catégorie **Integration**.
3. Recherchez **Alarme Manager Community** et installez-le.
4. Redémarrez Home Assistant.
5. Ouvrez **Paramètres → Appareils et services → Ajouter une intégration**.
6. Recherchez **Alarme Manager Community**.
7. Sélectionnez Alarmo / votre centrale et les équipements à superviser.
8. Gardez **OBSERVATION** pour les premiers essais.

### Option 2 — ZIP

Téléchargement direct : **https://github.com/cybersquatbis/home-assistant-alarm-manager/archive/refs/heads/main.zip**

Copiez ensuite `custom_components/alarme_manager/` vers `/config/custom_components/alarme_manager/`, puis redémarrez Home Assistant.

## ✨ Nouveautés 0.2

- 💡 **état réel des lumières** sur le plan, même lorsque l'alarme est désarmée ;
- 💡 prise en charge d'éclairages exposés comme `light.*` **ou** `switch.*` ;
- 🟡 lumière ON = jaune + halo ;
- 🚨 pendant une intrusion, les éléments déclencheurs clignotent en rouge et les éclairages de réaction restent identifiables ;
- 🔥 **détecteurs de fumée individuels**, configurables depuis Home Assistant ;
- 🔥 une détection fumée reste surveillée même si Alarmo est désarmé ;
- 🔥 écran Incendie avec état individuel des détecteurs ;
- ⚠️ entités indisponibles visibles en gris ;
- 🧾 événements fumée ajoutés à l'historique.

Aucune entité personnelle, aucun téléphone, aucune pièce privée et aucun plan d'installation réelle ne sont fournis dans la Community.

## Alarmo ou Alarme Manager ?

**Alarmo reste la centrale** : armement, désarmement, modes, capteurs et déclenchement.

**Alarme Manager est la couche de supervision** : plan maison, contexte d'incident, santé des équipements, fumée/incendie, RF, historique, notifications et orchestration protégée des caméras, lumières et sirène.

Les deux sont complémentaires.

## Beta actuelle

- panneau latéral Home Assistant et plan maison générique ;
- ouvrants, mouvements, fumée, caméras, lumières, sirène, RF et équipements critiques configurables ;
- OBSERVATION par défaut et passage ACTIF avec confirmation ;
- historique local des 100 derniers incidents ;
- score de protection et détection des entités indisponibles ;
- surveillance RF / anti-brouillage basée sur les entités choisies ;
- simulation d'incident sans sortie physique ;
- tests manuels courts et confirmés ;
- captures caméra, notifications, lumières et sirène optionnelles lors d'une alarme ;
- profils `notify.*` stockables par le backend.

## Tester sans risque

Commencez en **OBSERVATION**, vérifiez les états sur le plan, simulez un incident, puis testez séparément les sorties. N'activez les réactions réelles qu'après validation de votre installation.

Les détecteurs de fumée sont supervisés visuellement indépendamment de l'état d'Alarmo. Cette beta ne remplace pas un dispositif incendie ou une alarme certifiés.

## Services

`alarme_manager.set_mode`, `alarme_manager.simulate_incident`, `alarme_manager.clear_history` et `alarme_manager.test_output`.

## Limites connues

Restent à enrichir : placement/édition graphique avancés des repères, corrélation avancée par zone, profils photo par téléphone, règles météo ouvrants/Velux, détection des doublons avec les automatisations externes et intégration RFPlayer dédiée.

## Documentation

[Installation](docs/INSTALLATION.md) · [Sécurité](docs/SECURITY.md) · [Confidentialité](docs/PRIVACY.md) · [Architecture](docs/ARCHITECTURE.md) · [Changelog](CHANGELOG.md)

## Licence

MIT — voir [LICENSE](LICENSE).
