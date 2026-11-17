import platform
from importlib.metadata import version, PackageNotFoundError

def package_version(name):
    try: return version(name)
    except PackageNotFoundError: return "not installed"

def environment_summary():
    return {"python":platform.python_version(),"qiskit":package_version("qiskit"),"qiskit-aer":package_version("qiskit-aer"),"platform":platform.platform()}
