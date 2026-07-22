from action import Attack, Critical, Heal


class Bot:

    NAME = "Example"

    STATS = {
        "health": 8,
        "attack": 5,
        "critical": 3,
        "heal": 4
    }

    FRIENDS = []

    def move(self, state):
        me = state["me"]

        enemies = [
            p for p in state["players"]
            if p["alive"]
            and p["name"] != self.NAME
            and (state["ffa"] or not p["is_teammate"])
        ]

        if not enemies:
            return Heal()

        if me["health"] <= 9:
            return Heal()

        for p in sorted(enemies, key=lambda x: x["health"]):
            if p["health"] <= 9:
                return Attack(p["name"])

        if me["critical_left"]:
            for p in sorted(enemies, key=lambda x: x["health"]):
                if p["health"] <= 14:
                    return Critical(p["name"])

        if state["ffa"]:
            target = min(enemies, key=lambda x: x["health"])
        else:
            target = max(enemies, key=lambda x: x["health"])

        return Attack(target["name"])