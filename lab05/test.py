#!/usr/bin/env python

import os
import signal
import subprocess

lab_dir_path = os.getcwd()
tests_dir_path = os.path.join(os.getcwd(), "tests")
logisim_path = os.path.join(os.getcwd(),"../tools/logisim")

logisim_env = os.environ.copy()
logisim_env["CS61C_TOOLS_ARGS"] = logisim_env.get("CS61C_TOOLS_ARGS", "") + " -q"

class TestCase():
  """
  Runs specified circuit file and compares output against the provided reference trace file.
  """

  def __init__(self, id, name):
    self.id = id
    self.name = name

  def get_circ_path(self):
    return os.path.join(tests_dir_path, f"{self.id}.circ")

  def get_expected_table_path(self):
    return os.path.join(tests_dir_path, f"reference-output/{self.id}.out")

  def get_actual_table_path(self):
    return os.path.join(tests_dir_path, f"student-output/{self.id}.out")

  def run(self):
    passed = False
    proc = None
    try:
      proc = subprocess.Popen([logisim_path, "-tty", "table,binary,tabs", self.get_circ_path()], stdout=subprocess.PIPE, env=logisim_env)

      with open(self.get_expected_table_path(), "r") as reference:
        passed = self.check_output(proc.stdout, reference)
        os.kill(proc.pid, signal.SIGTERM)
        if passed:
          return (True, "Matched expected output")
        else:
          return (False, "Did not match expected output")
    finally:
      try:
        os.kill(proc.pid, signal.SIGTERM)
      except Exception as e:
        pass
    return (False, "Errored while running test")

  def check_output(self, student, reference):
    passed = True
    student_lines = []
    while True:
      student_line = student.readline().decode("ascii", errors="ignore").strip()
      reference_line = reference.readline().strip()
      if reference_line == "":
        break
      student_lines.append(student_line)
      if student_line != reference_line:
        passed = False
    output_path = self.get_actual_table_path()
    os.makedirs(os.path.dirname(output_path), mode=0o755, exist_ok=True)
    with open(output_path, "w") as f:
      for line in student_lines:
        f.write(f"{line}\n")
    return passed



tests = [
  TestCase("ex1-test", "Exercise 1: Sub-Circuits"),
  TestCase("ex2-test", "Exercise 2: Add Machine"),
  TestCase("ex3-test", "Exercise 3: FSM"),
  TestCase("ex4-test", "Exercise 4: Splitter"),
  TestCase("ex5-test", "Exercise 5: Rotate"),
]

def run_tests(tests):
  print("Testing files...")
  tests_failed = 0
  tests_passed = 0

  for test in tests:
    did_pass, reason = test.run()
    if did_pass:
      print(f"\tPASSED test: {test.name}")
      tests_passed += 1
    else:
      print(f"\tFAILED test: {test.name} ({reason})")
      tests_failed += 1

  print(f"Passed {tests_passed}/{tests_failed + tests_passed} tests")

if __name__ == '__main__':
  run_tests(tests)
