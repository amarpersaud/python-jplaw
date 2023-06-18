class Community:
    def __init__(self, lem, instance, community_name):
        self.lem = lem
        self.instance = instance
        self.community_name = community_name
        self.json = lem.getCommunity(instance, community_name)