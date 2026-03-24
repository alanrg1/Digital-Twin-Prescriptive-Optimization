import sys
import gurobipy as gp
from gurobipy import GRB

# | Created to verify if your environment is set for both NIST and Gurobi | #

def run_environment_check():
    print("___Environment Check___")

    # Check Gurobi License & Solver
    print("\nChecking Gurobi Optimization Solver...")
    try:
        # Create a dummy model to test the license
        m = gp.Model("license_test")
        x = m.addVar(vtype=GRB.BINARY, name="x")
        m.setObjective(x, GRB.MAXIMIZE)
        m.optimize()
        print("\nGurobi is installed and the license is active.")
    except gp.GurobiError as e:
        print(f"Gurobi Error: {e}")
        print("Action Required: Ensure you have requested and activated license.")

    # Check SimPROCESD Import
    print("\nChecking NIST SimPROCESD Framework...")
    try:
        # Appending the cloned folder to path so Python can find it
        sys.path.append('./simprocesd')
        import simprocesd
        print("NIST SimPROCESD successfully imported.")
    except ImportError:
        print("SimPROCESD not found. Did you clone the GitHub repo into this directory?")
        print("\nUse this: git clone https://github.com/usnistgov/simprocesd.git")

if __name__ == "__main__":
    run_environment_check()