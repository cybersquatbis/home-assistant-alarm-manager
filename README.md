# 🛡️ Alarme Manager Community

**Version 0.4.0-beta.1** pour Home Assistant.

Alarme Manager ajoute une couche de supervision visuelle autour d'une centrale existante, notamment Alarmo. La Community démarre en **OBSERVATION** et ne contient aucune entité, adresse e-mail, téléphone, nom de pièce ou plan privé.

## Nouveautés 0.4

- trajectoire live mouvements/ouvrants avec points numérotés et **Replay** ;
- effacement manuel de la trajectoire et nouvelle session après délai configurable ;
- températures par pièce ;
- taille des entités réglable globalement et par famille de **60 à 180 %** ;
- éditeur du plan avec déplacement direct des repères et coordonnées X/Y ;
- plan sans fond imposé par défaut : chacun peut fournir son image via `/local/...` ;
- ouvrants, mouvements, fumée, caméras, lumières, sirène, RF, équipements critiques, moteur de garage, chauffe-eau et autres équipements auxiliaires ;
- contact/sabotage garage affiché avec un symbole dédié lorsque son libellé correspond ;
- mode Plan Maxi plein écran ;
- score de protection et liste des entités indisponibles ;
- historique d'incidents, captures caméra et réactions optionnelles conservés.

## Installation HACS

1. HACS → Intégrations → Dépôts personnalisés.
2. Ajouter `https://github.com/cybersquatbis/home-assistant-alarm-manager` en catégorie **Integration**.
3. Installer **Alarme Manager Community**.
4. Redémarrer Home Assistant.
5. Paramètres → Appareils et services → Ajouter une intégration → **Alarme Manager Community**.
6. Configurer ses propres entités puis tester d'abord en **OBSERVATION**.

## Installation manuelle

Copier `custom_components/alarme_manager/` dans `/config/custom_components/alarme_manager/`, redémarrer Home Assistant puis faire un rafraîchissement forcé du navigateur.

## Confidentialité

Cette branche Community n'embarque aucune donnée de l'installation privée utilisée pendant le développement. Le plan est vide par défaut ; l'utilisateur choisit son propre fond et positionne ses repères localement.

## Sécurité

Alarme Manager Community n'est pas un système d'alarme certifié. Les réactions physiques doivent être activées volontairement après validation des capteurs et sorties.

Licence MIT.
