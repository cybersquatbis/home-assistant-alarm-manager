# Architecture Community

`config_flow.py` sélectionne les entités ; `engine.py` écoute les états et orchestre les incidents ; `storage.py` conserve mode, règles, profils et historique ; `websocket.py` relie le panneau au backend ; `frontend.py` enregistre le panneau ; les plateformes sensor/binary_sensor exposent la supervision dans Home Assistant.

Lorsqu'une centrale configurée passe à `triggered`, le moteur enregistre le contexte. En OBSERVATION aucune sortie physique n'est commandée. En ACTIF seules les réactions explicitement autorisées sont exécutées.
