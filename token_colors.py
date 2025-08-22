###############################################################################
############################ OPTIMIZATION WITH GUROBI #########################
###############################################################################
# assigns each token a consistent background color (using a hash + fixed color palette) 
# so tokens are visually different in color.

import hashlib

# General
PALETTE = [
    "#e6194B", "#3cb44b", "#ffe119", "#4363d8", "#f58231",
    "#911eb4", "#46f0f0", "#f032e6", "#bcf60c", "#fabebe",
    "#008080", "#e6beff", "#9A6324", "#fffac8", "#800000",
    "#aaffc3", "#808000", "#ffd8b1", "#000075", "#808080",
]


def color_for_token(token_str: str) -> str:
    # Deterministically map a token string to a color from PALETTE
    h = hashlib.md5(token_str.encode("utf-8")).hexdigest()
    idx = int(h[:8], 16) % len(PALETTE)
    return PALETTE[idx]
