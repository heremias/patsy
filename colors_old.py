class Color():
    RESET = "\033[0;0m"
    BOLD  = "\033[;1m"
    REVERSE = "\033[;7m"
    BLINK = "\033[;5m"

    # High Intensity
    BLACK='\033[0;90m'       # Black
    RED='\033[0;91m'         # Red
    GREEN='\033[0;92m'       # Green
    YELLOW='\033[0;93m'      # Yellow
    BLUE='\033[0;94m'        # Blue
    PURPLE='\033[0;95m'      # Purple
    CYAN='\033[0;96m'        # Cyan
    WHITE='\033[0;97m'       # White

    # Reset
    Color_Off="\[\033[0m\]"       # Text Reset

    # Underline = 4
    # Bold = 1

    # Various variables you might want for your PS1 prompt instead
    Time12h="\T"
    Time12a="\@"
    PathShort="\w"
    PathFull="\W"
    NewLine="\n"
    Jobs="\j"
    line = []
    def select(self):
        print("Select")

    def reset(self):
        print("Reset")
    