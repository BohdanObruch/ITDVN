import os


def resource(relative_path):
    import itdvn_project_tests
    from pathlib import Path

    resources_path = (
        Path(itdvn_project_tests.__file__)
        .parent
        .parent
        .absolute()
    )

    return (resources_path / relative_path).as_posix()

