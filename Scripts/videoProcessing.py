import numpy as np
import cv2

# Carregue o vídeo
cap = cv2.VideoCapture("../images/video.mp4")

# Enquanto houver frames no vídeo
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Converte o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Encontra pixels com valor acima de x
    x = 50
    ret, mask = cv2.threshold(gray, x, 255, cv2.THRESH_BINARY)

    # Encontra contornos nos pixels acima de x
    contours, hierarchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Se houver pelo menos um contorno
    if contours:
        # Encontra o maior contorno
        c = max(contours, key=cv2.contourArea)

        # Desenha o contorno do maior polígono
        polygon = cv2.approxPolyDP(
            c, epsilon=0.001 * cv2.arcLength(c, True), closed=True)

        # Preenche o interior do polígono com branco
        poly = np.ones(frame.shape, dtype=np.uint8) * 255
        cv2.fillPoly(poly, [polygon], (0, 0, 0))

        # Cria a máscara a partir do polígono preenchido
        result = cv2.bitwise_and(frame, poly)

        # Mostra o resultado
        cv2.imshow("Result", result)
        cv2.imshow("poly", poly)

    # Interrompe a exibição ao pressionar a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera o objeto de captura e destrói as janelas
cap.release()
cv2.destroyAllWindows()

"""
passo 1:
A partir de um raio entre o centro do frame e a sua borda, e para cada ângulo Theta entre zero e 2Pi fazer:
Para cada pixel branco mais distante do centro que for encontrado ao longo desse raio, fazer:
1 - guarda esse pixel (que chamaremos de 'a') no vetor de vertices no formato (x, y).
2 - Se já há um vertice 'b' no vetor de vértices, forma uma aresta com a seguinte extrutura [b, a] e guarda em um vetor de arestas.
3 - Se há pelo menos uma aresta no vetor de arestas, faz o seguinte:
    3.1 - Calcula a distância entre 'a' e 'b' e guarda na variável 'X'. 
    3.2 - Para cada vertice anterior 'c', calcula a distância entre 'a' e 'c'. 
    3.3 - Se essa distância for menor do que a 'X' e não há nenhuma aresta cruzando a linha entre 'a' e 'c', forma uma nova aresta entre 'a' e 'c' e destroi todas as outras arestas entre elas.

Ao finalizar o passo 1, verifica se o último vértice está ligado ao primeiro consultando o vetor de arestas.
Caso não esteja, forma uma última aresta entre o último vértice e o primeiro.
Com o vetor de vértices e arestas, formar um polígono fechado e retornar como uma máscara RGB, onde o interior tem valor 0 (preto) e o exterior tem valor 255 (branco).

Dict:

Para saber se duas arestas se cruzam, você pode usar o algoritmo de interseção de retas. Este algoritmo consiste em checar se as equações das retas formadas pelas arestas se cruzam. Para isso, é preciso calcular as equações das retas formadas pelos pontos de cada aresta e checar se elas se cruzam. Se as retas se cruzarem, significa que as arestas se cruzam também.

Existem diversas maneiras de calcular a equação de uma reta dado dois pontos. Uma maneira é usar a fórmula da reta, y = mx + b, onde m é a inclinação da reta e b é o intercepto. Para calcular m e b, você pode usar a seguinte equação:

m = (y2 - y1) / (x2 - x1)
b = y1 - m * x1

Com as equações das retas, você pode checar se elas se cruzam usando a seguinte fórmula:

x = (b2 - b1) / (m1 - m2)
y = m1 * x + b1

Se x e y estiverem dentro dos limites das retas, significa que as retas se cruzam.

-----------------------------------------------------------------------------------------------------------

Uma possível forma de implementar essa função seria usando o método "intersect" da biblioteca Shapely.

Esta biblioteca permite verificar interseções entre diferentes tipos de geometrias, incluindo linhas.

Aqui está uma exemplo de como verificar se duas arestas se cruzam:

from shapely.geometry import LineString

def intersect(edge1, edge2):
    line1 = LineString([edge1[0], edge1[1]])
    line2 = LineString([edge2[0], edge2[1]])
    return line1.intersects(line2)

Para fins de aprendizado, como seria a função anterior sem a utilização de bibliotecas externas?

"""
