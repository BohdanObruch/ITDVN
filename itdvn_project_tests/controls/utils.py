def resource(relative_path):
    import itdvn_project_tests
    from pathlib import Path
    return (
        Path(itdvn_project_tests.__file__)
        .parent
        .parent
        .joinpath('resources/')
        .joinpath(relative_path)
        .absolute()
        .__str__()
    )
