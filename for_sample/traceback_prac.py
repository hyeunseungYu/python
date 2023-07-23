# import sys, traceback

# def run_user_code(envdir):
#     source = input(">>> ")
#     try:
#         exec(source, envdir)
#     except Exception:
#         print("Exception in user code:")
#         print("-"*60)
#         traceback.print_exc(file=sys.stdout)
#         print("-"*60)

# envdir = {}
# while True:
#     run_user_code(envdir)

import traceback


def a():
    return 1/0


def b():
    a()


def main():
    try:
        b()
    except Exception as e:
        print("오류가 발생했습니다. : ", str(e))
        # print(traceback.format_exc())


main()