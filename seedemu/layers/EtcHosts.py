from seedemu.core import Emulator, Layer


class EtcHosts(Layer):
    """!
    @brief The EtcHosts layer.

    This layer setups host names for all nodes.
    """

    def __init__(self):
        """!
        @brief EtcHosts Layer constructor
        """
        super().__init__()
        self.addDependency('Base', False, False)

    def getName(self) -> str:
        return "EtcHosts"

    def render(self, emulator: Emulator):
        hosts_file_content = ""
        nodes = []
        reg = emulator.getRegistry()
        for ((scope, type, name), node) in reg.getAll().items():
            if type in ['hnode', 'snode', 'rnode', 'rs']:
                hosts_file_content += f"{node.getIPAddress()} {' '.join(node.getHostNames())}\n"
                nodes.append(node)
        
        for node in nodes:
            node.appendStartCommand(f"echo '{hosts_file_content}' >> /etc/hosts")
