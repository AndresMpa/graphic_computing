# BASIC OBJECT AS 3D FOR PRACTICE

# Up & down

Up = [[200, -600], [150, -700], [-300, -500], [0, -200]]

########################################################################################################################
########################################################################################################################

# FIGURE AS A 3D OBJECT

# Front & Back

# Figure one
BigCube_Front = [[200, 200], [200, -400], [-200, -400], [-200, 200]]
BigCube_Back = [[200, 200], [200, -400], [-200, -400], [-200, 200]]

# Figure two
FaceFront_Right = [[400, 200], [400, -100], [200, -100], [200, 200]]
FaceBack_Right = [[400, 200], [400, -100], [200, -100], [200, 200]]

# Figure three
FaceFront_Left = [[-200, 200], [-200, -100], [-400, -100], [-400, 200]]
FaceBack_Left = [[-200, 200], [-200, -100], [-400, -100], [-400, 200]]

# Sides

# Figure one
BigCube_Right = [[200, 200], [200, -400], [200, -400], [200, 200]]
BigCube_Left = [[-200, 200], [-200, -400], [-200, -400], [-200, 200]]

# Figure two
FaceRight_Right = [[400, 200], [400, -100], [400, -100], [400, 200]]
FaceLeft_Right = [[200, 200], [200, -100], [200, -100], [200, 200]]

# Figure three
FaceRight_Left = [[-200, 200], [-200, -100], [-200, -100], [-200, 200]]
FaceLeft_Left = [[-400, 200], [-400, -100], [-400, -100], [-400, 200]]

# Up & Down

# Figure one
BigCube_Up = [[200, -400], [-200, -400], [-200, -400], [200, -400]]
BigCube_Down = [[200, 200], [-200, 200], [-200, 200], [200, 200]]

# Figure two
FacetUp_Right = [[400, -100], [200, -100], [200, -100], [400, -100]]
FaceDown_Right = [[400, 200], [200, 200], [200, 200], [400, 200]]

# Figure three
FaceUp_Left = [[-200, -100], [-400, -100], [-400, -100], [-200, -100]]
FaceDown_Left = [[-200, 200], [400, 200], [-400, 200], [-200, 200]]

# Big cube
Figure_1 = [BigCube_Front, BigCube_Back, BigCube_Right, BigCube_Left, BigCube_Up, BigCube_Down]

# Small right
Figure_2 = [FaceFront_Right, FaceBack_Right, FaceRight_Right, FaceLeft_Right, FacetUp_Right, FaceDown_Right]

# Small left
Figure_3 = [FaceFront_Left, FaceBack_Left, FaceRight_Left, FaceLeft_Left, FaceUp_Left, FaceDown_Left]
