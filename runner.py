def simulation_one():
    pass

SIMULATION_LIST = [simulation_one]

def main():
    for simulation in SIMULATION_LIST:
        simulation()

if __name__ == "__main__":
    main()