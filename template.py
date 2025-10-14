import os
from pathlib import Path

project_name = "heart-failure"

file_list = [
    f"{project_name}/__init__.py",
    f"{project_name}/component/__init__.py",
    f"{project_name}/component/data_ingestion.py",
    f"{project_name}/component/data_transformation.py",
    f"{project_name}/component/model_training.py",
    f"{project_name}/component/model_evaluation.py",
    f"{project_name}/component/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore"
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml"
]

for filepath in file_list:
    file_path = Path(filepath)
    filedir, filename = os.path.split(file_path)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
    else:
        print(f"file is already present at: {file_path}.")