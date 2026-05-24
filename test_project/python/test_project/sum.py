from test_project.test_project import sum_as_string

def print_sum_as_string(a: int , b: int, /) -> None:
    """Coerce CLI args into rust and back out again.

    The / arg is for tyro, it makes a and b positional arguments instead of named ones.
    """
    print(sum_as_string(a, b))

def main() -> None:
    import tyro
    tyro.cli(print_sum_as_string)