






if __name__ == '__main__':
    
    import sys,os
    # sys.path.clear()
    # sys.path.append('/Desktop/Projetos/Maxbot/')
    from ..server.src.utils.RobotLed.robot import Robot

    print(sys.path)
    
    # from ..RobotLed.Faces import (
    #     desenho_feliz_quadrado,
    #     desenho_triste_quadrado,
    #     desenho_falando,
    #     desenho_distraido,
    #     desenho_normal
    # )

    param = sys.argv[1]

    if param =='feliz':
        robo = Robot()
        robo.draw_robot(desenho_feliz_quadrado)

    elif param == 'triste':
        robo = Robot()
        robo.draw_robot(desenho_triste_quadrado)

    elif param == 'livre':
        robo = Robot()
        robo.draw_robot_multiple(desenho_distraido,2,True)

    elif param == 'p-esquerda':
        robo = Robot()
        robo.piscar_olho('0',desenho_normal)

    elif param == 'p-direita':
        robo = Robot()
        robo.piscar_olho('1',desenho_normal)

    elif param == 'default':
        robo = Robot()
        robo.draw_robot_multiple(desenho_falando)
