from .bocas import *
from .olhos import *



desenho_feliz = desenho_olhar_curvado + desenho_boca_feliz
desenho_feliz_quadrado = desenho_olhar_quadrado + desenho_boca_feliz
desenhi_feliz_retangulo = desenho_olhar_retangulo + desenho_boca_feliz
desenho_feliz_esquerda = desenho_olhar_esquerda+ desenho_boca_feliz
desenho_feliz_direita = desenho_olhar_direita + desenho_boca_feliz

desenho_triste = desenho_olhar_curvado + desenho_boca_triste
desenho_triste_quadrado = desenho_olhar_quadrado + desenho_boca_triste 

desenho_normal = desenho_olhar_quadrado + desenho_boca_reta

desenho_normal_reto = desenho_olhar_reto + desenho_boca_reta
desenho_normal_robo = desenho_olhar_caido + desenho_boca_feliz_pequena

desenho_surpreso = desenho_olhar_quadrado + desenho_boca_surpreso

desenho_surpreso_esquerda = desenho_olhar_esquerda+desenho_boca_surpreso

desenho_surpreso_direita = desenho_olhar_direita+desenho_boca_surpreso

desenho_alegre = desenho_olhar_curvado + desenho_boca_sorriso_grande

desenho_desconfiado_esquerda = desenho_olhar_esquerda + desenho_boca_reta

desenho_desconfiado_direita = desenho_olhar_direita + desenho_boca_reta 

desenho_feliz_canto_boca_esquerda = desenho_olhar_piscada_esquerda + desenho_boca_lateral_esquerda

desenho_feliz_canto_boca_direita = desenho_olhar_piscada_direita + desenho_boca_lateral_direita

desenho_falando = [desenho_olhar_quadrado+desenho_boca_fechada_total,
    desenho_olhar_quadrado+desenho_boca_semi_aberta,
    desenho_olhar_quadrado+desenho_boca_fechada_total,
    desenho_olhar_quadrado+desenho_boca_surpreso
]

desenho_distraido = [
    desenho_olhar_retangulo + desenho_boca_reta,
    desenho_olhar_direita + desenho_boca_reta,
    desenho_olhar_esquerda + desenho_boca_reta,
]

desenho_piscada_esquerda = desenho_olhar_piscada_esquerda + desenho_boca_lateral_esquerda
desenho_piscada_esquerda_movimento = [desenho_normal , desenho_piscada_esquerda]

desenho_piscada_direita = desenho_olhar_piscada_direita + desenho_boca_lateral_direita
desenho_piscada_direita_movimento = [desenho_normal , desenho_piscada_direita]


desenho_drip = [
    (2,1),(6,1),
    (1,2),(2,2),(5,2),(6,2),
    (0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),
    (0,5),(2,5),(5,5),(7,5),
    (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),
]