import os


def rename_files(get_projections, get_files):
    """
    Args:
    :param get_projections: (list)
    :param get_files: (list)
    """
    filenames = []

    for proj in get_projections:
        if " " in proj:
            proj = proj.replace(" ", "-")
        filenames.append(proj + "-worldmapgenerator.svg")

    for new_name, old_name in zip(filenames, get_files):
        if old_name != new_name:
            print("renaming {0} to {1}".format(old_name, new_name))
            os.rename(old_name, new_name)


places = ["France", "Kazakhstan", "New-Zealand", "Somalia"]

projection = ["Armadillo",
              "Azimuthal Equal Area",
              "Azimuthal Equidistant",
              "Conic Equidistant",
              "Cubic",
              "Cylindrical Stereographic",
              "Eckert 1",
              "Fahey",
              "Gringorten",
              "Healpix",
              "Mercator",
              "Sinusoid",
              "Stereographic",
              "Waterman Butterfly"]

for place in places:
    filepath = "/home/[USERNAME_HERE]/Pictures/%s" % place
    if not os.path.isdir(filepath):
        print("creating filepath for %s" % place)
        os.mkdir(filepath)
    os.chdir(filepath)
    files = os.listdir(filepath)
    files.sort()
    rename_files(projection, files)
