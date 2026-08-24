# Changelog

## 0.3.0-beta.1 — 2026-08-24

Nouvelle beta Community préparée à partir des retours de la version privée, sans reprendre aucune donnée personnelle :

- nouveau tableau de supervision sombre et premium ;
- nouveau plan maison blueprint entièrement générique ;
- éditeur graphique **Paramètres plan** avec déplacement direct des repères ;
- modification du nom, du type et des coordonnées X/Y des repères ;
- image de plan personnalisable et configuration persistée localement ;
- mode **Plan Maxi** avec sortie par bouton ou touche `Esc` ;
- filtres d'affichage pour les principales familles d'équipements ;
- états indisponibles affichés en ambre afin de distinguer panne et alarme ;
- rouge réservé aux vraies alertes intrusion / incendie ;
- affichage amélioré des lumières allumées et des réactions d'alarme ;
- nouvelle catégorie générique `aux_devices` pour chauffe-eau, moteur, prise pilotée et autres équipements techniques ;
- état ON des équipements auxiliaires affiché en orange ;
- équipements auxiliaires inclus dans la supervision de disponibilité ;
- capteur pluie inclus dans le diagnostic de disponibilité lorsqu'il est configuré ;
- panneau dédié aux équipements indisponibles ;
- traductions FR/EN et documentation mises à jour.

## 0.2.0-beta.1 — 2026-08-23

Nouvelle beta Community issue des retours de test de la branche privée, sans aucune entité ni donnée personnelle :

- état réel des éclairages visible en permanence sur le plan ;
- prise en charge des éclairages exposés en `light.*` ou `switch.*` ;
- lumière allumée en jaune avec halo ;
- réaction d'éclairage pendant une intrusion distinguée visuellement ;
- détecteurs de fumée configurables individuellement ;
- alerte fumée indépendante du mode Alarmo et enregistrée dans l'historique ;
- couche Incendie et état individuel des détecteurs dans le panneau ;
- intrusion / fumée en rouge clignotant et entités indisponibles en gris ;
- création visuelle générique des équipements configurés sans reprendre de plan ou d'entité privée.

## 0.1.0-beta.1 — 2026-08-23

Première beta Community installable : config flow, panneau latéral, plan générique, OBSERVATION par défaut, supervision Alarmo, ouvrants/mouvements/caméras/lumières/sirène/RF, score de protection, historique, simulation, tests protégés et réactions optionnelles.
