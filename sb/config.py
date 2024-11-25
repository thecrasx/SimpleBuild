from sb.toml_dump import TOMLWrite
import tomllib


class Config:
    def __init__(self) -> None:
        self.configDir = '.'
        self.data = None


    def load(self, dir: str = '.'):
        with open(f"{dir}/config.toml", "rb") as f:
            self.data = tomllib.load(f)

    
    def save(self):
        if self.data:
            with open(f"{self.configDir}/config.toml", "w") as f:
                TOMLWrite.dump(f, self.data)


    def makeFile(self, out_dir: str = '.'):
        config = {}

        config["main"] = ""
        config["output_path"] = ""
        config["cpp"] = True
        config["Include"] = {"paths ": []}
        config["Libraries"] = {"include": []}
        config["Other"] = {"other": ""}

        with open(f"{out_dir}/config.toml", "w") as f:
            TOMLWrite.dump(f, config)

        self.data = config


    def include(self, path: str):
        if self.data:
            self.data["include"]["paths"].append(path)