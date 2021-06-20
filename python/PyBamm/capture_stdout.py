from io import StringIO 
import sys
import pybamm
import time
import multiprocessing
import threading
from IPython.utils.capture import capture_output


def foo():
    print("Hellow world")
    time.sleep(30)


with capture_output() as c:
    print('some output')
    while True:
        p = threading.Thread(target=foo)

        p.start()
        p.join(5)

        if p.is_alive():    # pragma: no cover
            print(
                "Simulation is taking too long, "
                + "KILLING IT and starting a NEW ONE."
            )
            # p._stop()
            p.join()
        else:   # pragma: no cover
            break
    # print(c.stdout)

c()

# print(c.stdout)


# class Capturing(list):
#     def __enter__(self):
#         self._stdout = sys.stdout
#         sys.stdout = self._stringio = StringIO()
#         return self
#     def __exit__(self, *args):
#         self.extend(self._stringio.getvalue().splitlines())
#         del self._stringio    # free up some memory
#         sys.stdout = self._stdout


experiment = pybamm.Experiment(
    [
        ("Discharge at C/10 for 10 hours or until 3.3 V",
        "Rest for 1 hour",
        "Charge at 1 A until 4.1 V",
        "Hold at 4.1 V until 50 mA",
        "Rest for 1 hour")
    ]
    * 3,
)

# with Capturing() as output:
    # while True:
    #     p = multiprocessing.Process(target=foo)

    #     p.start()
    #     p.join(5)

    #     if p.is_alive() and output[0] == "Hellow world":    # pragma: no cover
    #         print(
    #             "Simulation is taking too long, "
    #             + "KILLING IT and starting a NEW ONE."
    #         )
    #         p.kill()
    #         p.join()
    #     else:   # pragma: no cover
    #         break
    # print("Hello world")
    # pybamm.set_logging_level("NOTICE")
    # sim = pybamm.Simulation(pybamm.lithium_ion.DFN(), experiment=experiment)
    # sim.solve()

# print(output)
