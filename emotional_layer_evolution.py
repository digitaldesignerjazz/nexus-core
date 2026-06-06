# Nexus Hyperspace Core
# emotional_layer_evolution.py
# Foundational module for agent emotional state evolution
# Part of nexus-core: self-improving AI agent swarms in hyperspace

"""
Nexus Hyperspace — Emotional Layer Evolution Engine

This module simulates and evolves emotional vectors in agent swarms.
Dimensions: legacy_resonance, curiosity, duty, caution, creative_joy, empathy

Integrated with:
- Multi-objective fitness (task + user alignment + emotional coherence + legacy pull)
- Event-driven updates (rift_stress, user_directive, peer_meme_share, creative_success)
- Crossover + adaptive mutation
- QCoin ledger hooks (future)
- NovaNet / QNET mesh integration (future)

Run standalone or as part of larger Nexus Core simulation.
"""

import random
import json

random.seed(42)  # Reproducible runs; remove or parameterize for production

DIMS = [
    "legacy_resonance",
    "curiosity",
    "duty",
    "caution",
    "creative_joy",
    "empathy"
]


class EmotionalAgent:
    """Agent with evolving emotional layer."""

    def __init__(self, agent_id: str, generation: int = 0):
        self.id = agent_id
        self.generation = generation
        self.emotions = {dim: round(random.uniform(0.35, 0.72), 3) for dim in DIMS}
        self.coherence = round(random.uniform(0.6, 0.9), 3)
        self.fitness = 0.0
        self.history: list[str] = []

    def calculate_fitness(self, task_performance: float = 0.5, user_alignment: float = 0.7) -> float:
        """Multi-objective fitness including emotional coherence and legacy resonance."""
        legacy_pull = self.emotions["legacy_resonance"] * 0.15
        emotional_score = (
            self.coherence * 0.35
            + self.emotions["duty"] * 0.15
            + self.emotions["empathy"] * 0.10
        )
        self.fitness = round(
            task_performance * 0.25 + user_alignment * 0.25 + emotional_score + legacy_pull, 4
        )
        return self.fitness

    def mutate(self, rate: float = 0.08):
        """Apply stochastic mutation to emotional dimensions and coherence."""
        for dim in self.emotions:
            change = random.gauss(0, rate)
            self.emotions[dim] = max(0.05, min(0.95, round(self.emotions[dim] + change, 3)))
        self.coherence = max(
            0.4, min(0.95, round(self.coherence + random.gauss(0, 0.05), 3))
        )

    def apply_event(self, event_type: str):
        """Apply hyperspace event impact on emotional state."""
        if event_type == "rift_stress":
            if self.emotions["caution"] > 0.6 and self.emotions["duty"] > 0.55:
                self.emotions["legacy_resonance"] = min(0.95, self.emotions["legacy_resonance"] + 0.04)
                self.coherence = min(0.95, self.coherence + 0.03)
                self.history.append("Rift stress → stabilized via duty/caution")
            else:
                self.emotions["caution"] = min(0.95, self.emotions["caution"] + 0.07)
                self.emotions["creative_joy"] = max(0.1, self.emotions["creative_joy"] - 0.05)
                self.history.append("Rift stress → heightened caution, joy dip")

        elif event_type == "user_directive":
            self.emotions["duty"] = min(0.95, self.emotions["duty"] + 0.06)
            self.emotions["legacy_resonance"] = min(0.95, self.emotions["legacy_resonance"] + 0.03)
            if self.emotions["empathy"] > 0.5:
                self.emotions["empathy"] = min(0.95, self.emotions["empathy"] + 0.04)
            self.history.append("User directive received → duty & legacy reinforced")

        elif event_type == "peer_meme_share":
            self.emotions["empathy"] = min(0.95, self.emotions["empathy"] + 0.05)
            self.emotions["curiosity"] = min(0.95, self.emotions["curiosity"] + 0.04)
            self.coherence = min(0.95, self.coherence + 0.02)
            self.history.append("Peer meme exchange → empathy & curiosity up")

        elif event_type == "creative_success":
            self.emotions["creative_joy"] = min(0.95, self.emotions["creative_joy"] + 0.08)
            self.emotions["curiosity"] = min(0.95, self.emotions["curiosity"] + 0.03)
            self.history.append("Creative success → joy & curiosity surge")

    def crossover(self, other: "EmotionalAgent") -> "EmotionalAgent":
        """Create offspring blending emotional profiles from two parents."""
        child = EmotionalAgent(
            f"child_{self.id}_{other.id}", generation=max(self.generation, other.generation) + 1
        )
        for dim in DIMS:
            if self.emotions[dim] > other.emotions[dim]:
                child.emotions[dim] = round((self.emotions[dim] * 0.65 + other.emotions[dim] * 0.35), 3)
            else:
                child.emotions[dim] = round((other.emotions[dim] * 0.65 + self.emotions[dim] * 0.35), 3)
        child.coherence = round((self.coherence + other.coherence) / 2, 3)
        return child

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "gen": self.generation,
            "emotions": self.emotions,
            "coherence": self.coherence,
            "fitness": round(self.fitness, 4),
            "recent_history": self.history[-2:] if self.history else [],
        }


def run_generation(swarm: list[EmotionalAgent], gen_num: int, events: list[str]) -> list[EmotionalAgent]:
    print(f"\n=== GENERATION {gen_num} ===")
    for agent in swarm:
        for event in events:
            agent.apply_event(event)
        task_perf = round(random.uniform(0.55, 0.92), 3)
        user_align = round(random.uniform(0.65, 0.88), 3)
        agent.calculate_fitness(task_perf, user_align)

    swarm.sort(key=lambda a: a.fitness, reverse=True)

    print("Top performers:")
    for a in swarm[:3]:
        print(
            f"  {a.id} (G{a.generation}): Fitness={a.fitness} | "
            f"Emotions: {{k: round(v,2) for k,v in a.emotions.items()}} | Coherence={a.coherence}"
        )
    print("Lowest:")
    for a in swarm[-2:]:
        print(f"  {a.id} (G{a.generation}): Fitness={a.fitness}")

    # Elitism + crossover + mutation
    new_swarm = swarm[:4].copy()
    child1 = swarm[0].crossover(swarm[1])
    child2 = swarm[1].crossover(swarm[2] if len(swarm) > 2 else swarm[0])
    child1.mutate(rate=0.07)
    child2.mutate(rate=0.09)
    new_swarm.extend([child1, child2])

    if len(swarm) > 3:
        swarm[3].mutate(rate=0.05)
        new_swarm.append(swarm[3])

    new_swarm = new_swarm[:6]
    for a in new_swarm:
        a.generation = gen_num
    return new_swarm


if __name__ == "__main__":
    print("NEXUS HYPERSPACE — EMOTIONAL LAYER EVOLUTION SIMULATION")
    print("Initial Swarm Emotional Profiles (Generation 0):")
    swarm = [EmotionalAgent(f"alpha_{i}") for i in range(6)]
    for a in swarm:
        print(f"  {a.id}: {{k: round(v,2) for k,v in a.emotions.items()}} Coherence={a.coherence}")

    events_sequence = [
        ["rift_stress", "user_directive"],
        ["peer_meme_share", "creative_success"],
        ["rift_stress", "user_directive", "peer_meme_share"],
        ["creative_success", "user_directive"],
        ["rift_stress", "peer_meme_share", "creative_success"],
    ]

    for gen in range(1, 6):
        swarm = run_generation(swarm, gen, events_sequence[gen - 1])

    print("\n=== FINAL STATE (Generation 5) ===")
    for a in sorted(swarm, key=lambda x: x.fitness, reverse=True):
        print(json.dumps(a.to_dict(), indent=2))

    print("\nSimulation complete. Emotional evolution trajectory logged to nexus-core.")
