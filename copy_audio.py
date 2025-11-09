import shutil


SRC = "audio/audio.wem"
OUT = "audio/"
WEM = [
    "1038719001.wem", 
    "1052911782.wem", 
    "193250534.wem", 
    "212033934.wem", 
    "228132900.wem", 
    "521504529.wem", 
    "533464258.wem", 
    "634636526.wem", 
    "731319179.wem", 
    "835783005.wem", 
    "964673994.wem"
]


for wem in WEM:
    shutil.copy(SRC, OUT + wem)
