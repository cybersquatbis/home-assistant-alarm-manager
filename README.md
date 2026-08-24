# 🛡️ Alarme Manager Community

**Alarme Manager Community** est une intégration personnalisée pour **Home Assistant** qui ajoute une couche de supervision et d'orchestration autour d'une centrale existante, notamment **Alarmo**.

> **Beta communautaire ouverte aux tests — 0.3.0-beta.1.** Le moteur démarre en **OBSERVATION**. Les réactions physiques automatiques sont désactivées par défaut et doivent être autorisées explicitement.

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

## ✨ Nouveautés 0.3

- 🖥️ **nouveau tableau de supervision sombre et premium**, dérivé des retours terrain de la version privée mais entièrement générique ;
- 🗺️ **nouveau plan maison blueprint générique** fourni par défaut ;
- ✏️ **Paramètres plan** : déplacement des repères directement à la souris, modification du nom, du type et des coordonnées X/Y ;
- 🖼️ possibilité d'utiliser sa propre image de plan via son URL Home Assistant ;
- 💾 positions et configuration du plan enregistrées localement dans Home Assistant ;
- 🔎 **Plan Maxi** plein écran, avec sortie par bouton ou touche `Esc` ;
- 🎚️ filtres du plan pour ouvrants, mouvements, caméras, lumières, fumée, équipements techniques, sirène et RF ;
- 🟢 états normaux sobres et lisibles ;
- ⚠️ entités indisponibles affichées en **ambre**, pour ne pas les confondre avec une alarme ;
- 🔴 rouge réservé aux vraies alertes intrusion / incendie ;
- 💡 éclairages `light.*` ou `switch.*` visibles en permanence avec état réel ;
- 🟡 lumière ON = jaune + halo ;
- 🔥 détecteurs de fumée individuels supervisés indépendamment de l'état d'Alarmo ;
- 🔌 catégorie **Équipements auxiliaires** pour chauffe-eau, moteur, prise pilotée ou autre équipement à surveiller ;
- ♨️ équipements auxiliaires actifs distingués visuellement en orange ;
- 📊 liste dédiée des équipements indisponibles et accès au détail de l'entité ;
- 🧾 historique local des incidents.

Aucune entité personnelle, aucun téléphone, aucune pièce privée et aucun plan d'installation réelle ne sont fournis dans la Community.

## Alarmo ou Alarme Manager ?

**Alarmo reste la centrale** : armement, désarmement, modes, capteurs et déclenchement.

**Alarme Manager est la couche de supervision** : plan maison, contexte d'incident, santé des équipements, fumée/incendie, RF, historique, notifications et orchestration protégée des caméras, lumières et sirène.

Les deux sont complémentaires.

## Beta actuelle

- panneau latéral Home Assistant et plan maison générique ;
- éditeur graphique des repères et image de plan personnalisable ;
- mode Plan Maxi et filtres d'affichage ;
- ouvrants, mouvements, fumée, caméras, lumières, équipements auxiliaires, sirène, RF et équipements critiques configurables ;
- OBSERVATION par défaut et passage ACTIF avec confirmation ;
- historique local des 100 derniers incidents ;
- score de protection et détection des entités indisponibles ;
- surveillance RF / anti-brouillage basée sur les entités choisies ;
- simulation d'incident sans sortie physique ;
- tests manuels courts et confirmés ;
- captures caméra, notifications, lumières et sirène optionnelles lors d'une alarme ;
- profils `notify.*` stockables par le backend.

## Équipements auxiliaires

La catégorie **Équipements auxiliaires** permet d'ajouter des entités qui ne sont pas directement des capteurs d'alarme : chauffe-eau, moteur, prise pilotée, équipement technique, etc.

Le panneau affiche leur état réel :

- **OFF / repos** : discret ;
- **ON / actif** : orange ;
- **unavailable / unknown** : ambre avec état de défaut.

Ces équipements ne déclenchent pas une intrusion par eux-mêmes. Ils sont supervisés visuellement et participent au diagnostic de disponibilité.

## Personnaliser le plan

Dans le panneau Alarme Manager, ouvrez **Paramètres plan**. Vous pouvez alors :

- déplacer les repères directement sur le plan ;
- ajuster précisément X/Y ;
- renommer un repère ;
- changer son type visuel ;
- remplacer le plan générique par votre propre image ;
- enregistrer le résultat dans le stockage local de l'intégration.

Les nouvelles entités configurées sont ajoutées automatiquement au plan et peuvent ensuite être repositionnées.

## Tester sans risque

Commencez en **OBSERVATION**, vérifiez les états sur le plan, simulez un incident, puis testez séparément les sorties. N'activez les réactions réelles qu'après validation de votre installation.

Les détecteurs de fumée sont supervisés visuellement indépendamment de l'état d'Alarmo. Cette beta ne remplace pas un dispositif incendie ou une alarme certifiés.

## Services

`alarme_manager.set_mode`, `alarme_manager.simulate_incident`, `alarme_manager.clear_history` et `alarme_manager.test_output`.

## Limites connues

Restent à enrichir : corrélation avancée par zone, profils photo par téléphone, règles météo ouvrants/Velux, détection des doublons avec les automatisations externes et intégration RFPlayer dédiée.

## Documentation

[Installation](docs/INSTALLATION.md) · [Sécurité](docs/SECURITY.md) · [Confidentialité](docs/PRIVACY.md) · [Architecture](docs/ARCHITECTURE.md) · [Changelog](CHANGELOG.md)

## Licence

MIT — voir [LICENSE](LICENSE).
