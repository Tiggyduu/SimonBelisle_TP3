    # Permet le Ctrl Z
    cmds.undoInfo(openChunk=True)

    try:

        for _ in range(10):
            print()

    finally:

        cmds.undoInfo(closeChunk=True)