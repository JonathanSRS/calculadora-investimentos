import os
from dotenv import load_dotenv
# Carrega o JAVA_HOME definido no seu arquivo .env

class EnvConfig:
    def __init__(self):
        pass
    
    load_dotenv() 
    # Valida e injeta o Java na memória do processo atual
    if "JAVA_HOME" in os.environ:
        # Insere o binário do Java no início do PATH para priorizar esta versão
        os.environ["PATH"] = (
            os.path.join(os.environ["JAVA_HOME"], "bin") 
            + os.pathsep 
            + os.environ["PATH"])
    else:
        raise RuntimeError("❌ Erro Crítico: JAVA_HOME não foi configurado no arquivo .env")

    # Validação Crítica do Hadoop
    if "HADOOP_HOME" in os.environ:
        hadoop_bin = os.path.join(os.environ["HADOOP_HOME"], "bin")
        os.environ["PATH"] = hadoop_bin + os.pathsep + os.environ["PATH"]
    else:
        raise RuntimeError("❌ Defina o HADOOP_HOME no arquivo .env para destravar o Windows")