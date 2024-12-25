from cog import BasePredictor, Input, File
from pathlib import Path
import subprocess

class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory to make running multiple predictions efficient"""

    def predict(
        self, 
        model_file: File = Input(description="3D model file in .glb format"),
        scale_percentage: float = Input(description="Scale percentage for -si", default=0.01),
        error_percentage: float = Input(description="Error percentage for -se", default=0.01)
    ) -> Path:
        """Run a single prediction on the model"""
        input_path = Path("input.glb")
        output_path = Path("output.glb")
        
        with open(input_path, "wb") as f:
            f.write(model_file.read())
        
        subprocess.run([
            "./core/gltfpack", 
            "-i", str(input_path), 
            "-o", str(output_path), 
            "-si", str(scale_percentage), 
            "-se", str(error_percentage),
            "-sv",
            "-slb",
        ], check=True)
        
        return Path(output_path)