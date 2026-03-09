"""
Plot a(t) for matter-dominated universes: closed, flat, and open.
Uses exact parametric/analytic solutions of the Friedmann equation.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# ── LaTeX-quality settings ──────────────────────────────────────
rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 14,
    "axes.labelsize": 16,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "lines.linewidth": 2.2,
})

fig, ax = plt.subplots(figsize=(6, 4))

# ── Closed (k > 0): cycloid ────────────────────────────────────
# a = A(1 - cos η),  t = A(η - sin η)
A_cl = 1.15
eta = np.linspace(0, 2 * np.pi, 800)
t_closed = A_cl * (eta - np.sin(eta))
a_closed = A_cl * (1 - np.cos(eta))
ax.plot(t_closed, a_closed, color="#c0392b", lw=2.5,
        label=r"closed ($k>0$)")

# ── Flat (k = 0): a ∝ t^{2/3} ──────────────────────────────────
t_end = 4.2
t_flat = np.linspace(0, t_end, 500)
a_flat = t_flat ** (2.0 / 3.0)
ax.plot(t_flat, a_flat, color="0.35", ls="--", lw=2.5,
        label=r"flat ($k=0$)")

# ── Open (k < 0): hyperbolic ───────────────────────────────────
# a = A(cosh η - 1),  t = A(sinh η - η)
A_op = 0.42
eta_op = np.linspace(0, 3.2, 600)
t_open = A_op * (np.sinh(eta_op) - eta_op)
a_open = A_op * (np.cosh(eta_op) - 1)
mask = t_open <= t_end
ax.plot(t_open[mask], a_open[mask], color="#2471a3", lw=2.5,
        label=r"open ($k<0$)")

# ── Annotations ─────────────────────────────────────────────────
ax.annotate(r"Big Bang", xy=(0, 0), xytext=(0.3, 0.5),
            fontsize=11, color="0.25",
            arrowprops=dict(arrowstyle="->", color="0.4", lw=1.0))

t_crunch = t_closed[-1]  # = 2πA
ax.annotate(r"Big Crunch", xy=(t_crunch, 0),
            xytext=(t_crunch - 1.4, 0.55),
            fontsize=11, color="#c0392b",
            arrowprops=dict(arrowstyle="->", color="#c0392b", lw=1.0))

# ── Axes ────────────────────────────────────────────────────────
ax.set_xlabel(r"$t$")
ax.set_ylabel(r"$a(t)$")
ymax = max(a_flat.max(), a_closed.max()) * 1.25
ax.set_xlim(0, max(t_end + 0.3, t_crunch * 1.06))
ax.set_ylim(0, ymax)
ax.set_xticks([])
ax.set_yticks([])
ax.legend(loc="upper left", fontsize=12, framealpha=0.9)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.tight_layout()
fig.savefig("/Users/sabiuc/teaching/Cosmology_course/notes/figures/at_matter.png",
            dpi=300, bbox_inches="tight")
print("Saved at_matter.png")
