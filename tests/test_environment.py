from qsynth_quantum.environment import environment_summary

def test_environment_summary_contains_core_fields():
    e=environment_summary()
    assert {"python","qiskit","qiskit-aer"} <= e.keys()
