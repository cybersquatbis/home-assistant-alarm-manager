# 🛡️ Alarme Manager Community

**Alarme Manager Community** est une intégration personnalisée pour **Home Assistant** dédiée à la supervision d'alarme, au plan maison interactif et à l'orchestration des équipements de sécurité.

> **Statut : beta communautaire.** Le moteur démarre toujours en **OBSERVATION**. Faites une sauvegarde Home Assistant avant installation ou mise à jour et validez vos notifications, caméras, éclairages et sirène avant toute activation réelle.

## ✨ Fonctions principales

- 🏠 **Plan Maison interactif** avec image personnalisable, vues Global / RDC / Étage et repères en drag & drop.
- 🚪 **Ouvrants** : portes, fenêtres, baies vitrées, porte-fenêtres, garage et Velux, avec polarité ON/OFF configurable.
- 👣 **Détecteurs de mouvement** organisables par zones et corrélables avec le périmètre.
- 📷 **Caméras** avec emplacements permanents indépendants du matériel : une caméra peut être remplacée sans refaire le plan.
- 📸 **Captures photo** et tests caméra depuis l'interface.
- 💡 **Éclairages de dissuasion** configurables par mode et horaires.
- 🚨 **Sirène** configurable avec garde-fous et durée maximale.
- 👨‍👩‍👧‍👦 **Profils de notification** : alertes, photos, critiques et messages techniques peuvent être séparés par téléphone.
- 📱 Détection des services `notify.mobile_app_*` présents sur Home Assistant.
- 🛡️ **Anti-sabotage / anti-brouillage** : surveillance RF, tamper, alimentation, réseau et équipements critiques.
- 📡 Préparation **RFPlayer** / anti-jamming et autres capteurs radio.
- 🌧️ **Météo locale / pluie** prévue pour protéger les ouvrants et Velux.
- 🧾 **Historique des incidents**, état de santé des équipements et score de protection.
- 🧪 **Zone Tests** pour valider les téléphones, photos, lumières et sirène avant activation.
- 🚫 Détection de configurations pouvant provoquer des réactions en double.
- 👀 **OBSERVATION par défaut** : aucune sortie n'est activée automatiquement à l'installation.

Alarmo peut rester votre centrale d'alarme. Alarme Manager peut être utilisé comme couche de supervision et d'orchestration autour d'une centrale existante.

## 🚀 Installation manuelle

1. Téléchargez le dépôt ou la dernière archive de beta.
2. Copiez `custom_components/alarme_manager/` dans `/config/custom_components/`.
3. Redémarrez Home Assistant.
4. Ouvrez **Paramètres → Appareils et services → Ajouter une intégration**.
5. Recherchez **Alarme Manager Community**.
6. Choisissez votre centrale d'alarme si vous en utilisez une.
7. Ouvrez **Alarme Manager** depuis la barre latérale.
8. Configurez les onglets dans cet ordre conseillé : **Ouvrants → Zones & caméras → Éclairages → Sirène → Plan Maison**.

Aucun `entity_id` personnel n'est fourni : la configuration se fait depuis l'interface Home Assistant.

## 🗺️ Plan Maison

Le paquet inclut un plan générique uniquement pour démarrer. Vous pouvez remplacer `custom_components/alarme_manager/plan_maison.jpg` par votre propre image en conservant le même nom, puis positionner les repères depuis le mode édition du plan.

Les repères et emplacements caméra restent indépendants des entités matérielles afin de faciliter les remplacements futurs.

## 🔐 Confidentialité

La branche Community est volontairement générique : aucune entité, aucun téléphone et aucun plan d'une installation privée ne sont inclus. Voir [`docs/PRIVACY.md`](docs/PRIVACY.md).

## ⚠️ Sécurité / beta

Alarme Manager Community est un projet communautaire et ne remplace pas un système d'alarme certifié. Avant toute activation réelle :

- faites une sauvegarde Home Assistant ;
- laissez le moteur en **OBSERVATION** ;
- testez les notifications ;
- testez les captures caméra ;
- testez les lumières ;
- testez la sirène sur place ;
- vérifiez vos capteurs et polarités.

## 🧪 Validation

Cette beta passe des contrôles statiques Python, JavaScript, JSON et YAML ainsi qu'un scan anti-données privées. Un test sur plusieurs installations Home Assistant réelles reste nécessaire avant de considérer la version stable.

## 💬 Retours

Les retours sont les bienvenus via les **Issues GitHub**. Merci d'indiquer :

- votre version de Home Assistant ;
- la version d'Alarme Manager ;
- le type de centrale utilisée ;
- le comportement attendu / observé ;
- les logs pertinents sans informations sensibles.

Voir aussi : [`CHANGELOG.md`](CHANGELOG.md) · [`docs/INSTALLATION.md`](docs/INSTALLATION.md) · [`COMMUNAUTE_FB.md`](COMMUNAUTE_FB.md)
