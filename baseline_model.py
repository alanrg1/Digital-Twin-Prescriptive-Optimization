import sys

# Ensure Python knows where to find the cloned repo
# (You may not need this if your IDE path is already set)
sys.path.append('./simprocesd')

from simprocesd.model import System
from simprocesd.model.factory_floor import Source, PartProcessor, Buffer, Sink

def run_baseline():
    print("___Initializing 3-Machine Baseline Simulation___\n")

    # 1. Initialize the master system clock
    system = System()

    # 2. Build the line using Upstream Mapping

    # The starting point
    source = Source()

    # Machine 1 pulls directly from the Source
    m1 = PartProcessor(upstream=[source], cycle_time=2.5)

    # Buffer 1 sits after M1 with a strict capacity of 1 unit
    b1 = Buffer(upstream=[m1], capacity=1)

    # Machine 2 pulls from Buffer 1 (This is mathematically our Bottleneck)
    m2 = PartProcessor(upstream=[b1], cycle_time=2.8)

    # Buffer 2 sits after M2 with a strict capacity of 1 unit
    b2 = Buffer(upstream=[m2], capacity=1)

    # Machine 3 pulls from Buffer 2
    m3 = PartProcessor(upstream=[b2], cycle_time=2.4)

    # The Sink acts as the final destination, pulling from M3
    sink = Sink(upstream=[m3])

    # 3. Run the engine for 40 hours (40 hours * 60 minutes = 2400 minutes)
    print("Executing simulation for 2400 simulated minutes...")
    system.simulate(simulation_duration=2400)

    # 4. Confirm completion
    print("The simulation ran without errors.")
    print("Baseline manufacturing logic has been successfully established.")

if __name__ == "__main__":
    run_baseline()