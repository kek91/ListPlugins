from fman import DirectoryPaneCommand, load_json, show_alert
from os import getenv, path
import platform
import glob

class ListPlugins(DirectoryPaneCommand):
    def __call__(self):
        if platform.system() == "Windows":
            appdata = getenv('APPDATA')
        elif platform.system() == "Linux":
            appdata = path.expanduser("~") + "/.config"
        elif platform.system() == "Darwin":
            appdata = path.expanduser("~") + "/Library/Application Support"

        plugin_dir = glob.glob(appdata + "/fman/Plugins/*")
        plugin_amount = 0
        plugins = []
        plugins_ignore = ['User']
        for p in plugin_dir:
            if path.isdir(p):
                p = path.basename(p)
                if p not in plugins_ignore:
                    plugin_amount += 1
                    plugins.append(p)
        output = "Plugins\n\n"
        output += "Currently installed plugins: (" + str(plugin_amount) + ")\n\n"
        for p in plugins:
            output += str(p) + "\n"
        show_alert(output)
