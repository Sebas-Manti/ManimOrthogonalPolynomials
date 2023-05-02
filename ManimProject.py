import math

import matplotlib.pyplot as plt
from scipy.special import legendre
import numpy as np
from manim import *


class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)


class MyScene(Scene):
    def construct(self):
        imagen = ImageMobject("konrad_logo.png")

        # Ajusta el tamaño de la imagen
        imagen.scale(0.8)

        # Crea el título y el subtítulo utilizando la clase TextMobject
        titulo = Tex('Historias de los polinomios ortogonales')
        subtitulo = Tex('Por: Sebastian Mantilla Manzano')

        # Ajusta el tamaño del título y el subtítulo
        titulo.scale(1.2)
        subtitulo.scale(0.7)
        titulo.set_color(WHITE)
        subtitulo.set_color(WHITE)
        # Posiciona el título y el subtítulo
        titulo.move_to(UP * 2)
        subtitulo.move_to(UP * 1.3)

        # Aparece la imagen en el centro de la pantalla durante el primer segundo
        self.play(FadeIn(imagen), run_time=1)

        # Se queda la imagen durante un segundo
        self.wait(1.5)

        self.play(imagen.animate.to_corner(DR), run_time=2)

        # Aparece el título y el subtítulo
        self.play(Write(titulo), Write(subtitulo))

        # Se queda el título y el subtítulo durante un segundo
        self.wait(3.5)

        # Desvanece todo a negro
        self.play(FadeOut(imagen), FadeOut(titulo), FadeOut(subtitulo), run_time=1.3)

        # Crea la imagen utilizando la clase ImageMobject

        france = ImageMobject("france.png")
        france.scale(0.3)
        decada = MathTex("1970s")
        decada.scale(0.8)
        decada.to_corner(UL)

        self.wait(3)
        self.play(france.animate)
        self.wait(1)
        self.play(Write(decada))
        self.play(FadeOut(france), run_time=1)

        #Oil tower
        oilTower = ImageMobject("oilTower.png")
        oilTower.scale(0.4)
        self.play(FadeIn(oilTower), run_time=0.8)
        self.play(oilTower.animate.to_corner(UP), run_time=0.7)
        self.wait(2)


        path = Line(LEFT*5, RIGHT*5)
        path.points[1:3] += UP*2
        self.play(Create(path))
        self.wait(2)

        line = Line([0, 2.5, 0], [0, 0, 0]).set_color(RED)
        self.play(Create(line), run_time=2)
        # create the text object
        x = Text("X", font_size=72, font="Arial", color=PURE_RED, weight=BOLD)

        # create the animations
        fade_in1 = FadeIn(x, rate_func=there_and_back, run_time=1)
        fade_out1 = FadeOut(x, rate_func=there_and_back, run_time=1)

        # animate the text
        self.wait(3)
        self.play(fade_in1)
        self.play(fade_out1)
        self.play(FadeOut(oilTower), FadeOut(line), FadeOut(decada))
        self.play(path.animate.move_to(UP*1))
        self.wait(3)

        dot1 = Dot(path.point_from_proportion(0.6), radius=0.3, color=BLUE)
        dot2 = Dot(path.point_from_proportion(0.8), radius=0.3, color=BLUE)
        self.play(Create(dot1), Create(dot2))
        self.wait(4)

        # create explosion shape
        circle1 = Circle(radius=0.05, fill_opacity=1, color=YELLOW_A)
        circle2 = Circle(radius=0.1, fill_opacity=0.8, color=YELLOW)
        circle3 = Circle(radius=0.15, fill_opacity=0.6, color=ORANGE)
        circle4 = Circle(radius=0.2, fill_opacity=0.4, color=PURE_RED)
        circle5 = Circle(radius=0.25, fill_opacity=0.2, color=RED)
        explosion = VGroup(circle1, circle2, circle3, circle4, circle5)
        explosion.scale(2)
        explosion.move_to(path.get_start())

        # animate explosion
        self.play(GrowFromCenter(explosion))
        self.wait(1)

        path2 = Line(LEFT*5, RIGHT*5, color=GRAY)
        path2.points[1:3] += UP*2
        path2.move_to(DOWN*2)

        path3 = Line(LEFT*5, RIGHT*5, color=GRAY)
        path3.points[1:3] += UP*2
        path3.move_to(DOWN*3.3)

        pDot2 = Dot(path2.point_from_proportion(0.5))
        pDot3 = Dot(path3.point_from_proportion(0.8))

        p1_start = path.get_start()
        p1_end = pDot2.get_start()
        p2_start = path.get_start()
        p2_end = pDot3.get_start()
        p3_end = dot1.get_start()
        p4_end = dot2.get_start()

        c_func1 = lambda t: p1_start + np.sin(50*t)*1/14 + t*(p1_end-p1_start)
        sin_func_1 = ParametricFunction(
            lambda t: np.array([c_func1(t)[0], c_func1(t)[1], np.sin(12*t)*1/14]),
            color=YELLOW,
        )

        c_func2 = lambda t: p2_start + np.sin(70*t)*1/14 + t*(p2_end-p2_start)
        sin_func_2 = ParametricFunction(
            lambda t: np.array([c_func2(t)[0], c_func2(t)[1], np.sin(12*t)*1/14]),
            color=YELLOW,
        )

        c_func3 = lambda t: sin_func_1.get_end() + np.sin(50*t)*1/14 + t*(dot1.get_center()-sin_func_1.get_end())
        sin_func_3 = ParametricFunction(
            lambda t: np.array([c_func3(t)[0], c_func3(t)[1], np.sin(np.cos(12*t))*1/14]),
            color=BLUE,
        )

        c_func4 = lambda t: sin_func_2.get_end() + np.sin(70*t)*1/14 + t*(dot2.get_center()-sin_func_2.get_end())
        sin_func_4 = ParametricFunction(
            lambda t: np.array([c_func4(t)[0], c_func4(t)[1], np.sin(12*t)*1/14]),
            color=BLUE,
        )
        tierra = Tex("Tierra", color=GRAY)
        tierra.move_to(path.get_center(), DOWN)
        rocas  = Tex("Rocas", color= GRAY)
        rocas.move_to(DOWN)
        petroleo = Tex("Petroleo", color=GRAY)
        petroleo.move_to(path3.get_center(), DOWN*0.1)
        self.play(Create(sin_func_1), Create(sin_func_2), run_time=5)
        self.play(Create(sin_func_3), Create(sin_func_4), run_time=5)
        self.play(FadeIn(path2), FadeIn(path3), Write(tierra), Write(rocas), Write(petroleo), run_time=3)
        self.wait(5)
        self.play(
            FadeOut(path),
            FadeOut(path2),
            FadeOut(path3),
            FadeOut(explosion),
            FadeOut(dot1),
            FadeOut(dot2),
            FadeOut(sin_func_1),
            FadeOut(sin_func_2),
            FadeOut(sin_func_3),
            FadeOut(sin_func_4),
            FadeOut(tierra),
            FadeOut(rocas),
            FadeOut(petroleo),
            run_time=2
        )
        nText = Tex("Pero...\n ¿Qué tiene que ver esto con los polinomios Ortogonales?")
        self.play(Write(nText), run_time=7)
        self.wait(3)
        veamos = Tex("Veamos:")
        veamos.to_corner(UL)
        self.play(Transform(nText, veamos), run_time=2)
        self.wait(2)

        ortoT = Tex("Ortogonalidad")
        ortoT.move_to(UP*1)
        self.play(Write(ortoT), run_time=2)
        self.play(FadeOut(ortoT))
        ax = NumberPlane()

        arrow1 = Vector([2, 2], color=GREEN)
        arrow2 = Vector([3, -3], color=PURE_RED)
        aLable = Tex("a", color=GREEN)
        bLable = Tex("b", color=PURE_RED)
        aLable.next_to(arrow1)
        bLable.next_to(arrow2)
        dot = Dot()
        vectors = VGroup(arrow1, arrow2, dot, aLable, bLable)
        self.play(Create(vectors), FadeIn(ax), run_time=2)

        self.play(FadeOut(ax), vectors.animate.move_to(LEFT*5).rotate(45 * DEGREES).scale(0.8), run_time=2)
        self.wait(5)
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            x_axis_config={
                "numbers_to_include": np.arange(0, 5.01, 2),
                "numbers_with_elongated_ticks": np.arange(0, 5.01, 2),
            },
            tips=False,
        )
        axes.move_to(RIGHT * 4).scale(0.7)
        self.play(Create(axes), Rotate(arrow1, angle=-PI/2, about_point=dot.get_center(), rate_func=linear), run_time=3)
        self.wait(4)

        cos_graph = axes.plot(lambda x: np.cos(x), x_range=[0, PI/2], color=GREEN)
        angle = DecimalNumber().set_color(WHITE)
        res =DecimalNumber().set_color(WHITE)
        cos = MathTex("\\cos(")
        theta = MathTex("\\theta")
        cl = MathTex(") = ")
        y = MathTex("y")
        theta.next_to(cos)
        cl.next_to(theta)
        y.next_to(cl)
        ecu = VGroup(cos, theta, cl, y)
        ecu.move_to(UP*3)
        self.play(Write(ecu), run_time=2)

        angle.next_to(cos)
        cl.next_to(angle)
        res.next_to(cl)
        ecu2 = VGroup(cos, angle, cl, res)

        self.play(TransformMatchingShapes(ecu, ecu2), run_time=2)
        self.play(
            Count(angle, 0, 90),
            Count(res, 1, 0),
            Rotate(arrow1, angle=PI/2, about_point=dot.get_center(), rate_func=linear),
            Create(cos_graph),
            run_time=4,
            rate_func=linear)
        self.wait(2)

        self.play(FadeOut(vectors), FadeOut(axes), FadeOut(cos_graph), run_time=2)
        self.wait(3)

        defin = Tex("\\textbf{Def: }")
        espacio = MathTex("v, w \\in V,")
        ortodef = Tex(" v y w son ortogonales si ")
        fin = MathTex("\\langle v \\cdot w \\rangle = 0")
        defin.move_to(LEFT)
        espacio.next_to(defin)
        ortodef.next_to(espacio)
        fin.next_to(ortodef)
        nDef = VGroup(defin, espacio, ortodef, fin)
        nDef.move_to(ORIGIN)
        self.play(Write(nDef), run_time=3)
        self.wait(2)
        self.play(FadeOut(nDef), run_time=2)

        self.play(FadeOut(ecu2), FadeOut(angle), FadeOut(res))
        self.play(FadeOut(nText))
        self.wait(2)

        #Polinómios de Lagendre
        nText = Tex("Cómo se ve entonces")
        nText1 = Tex("la ortogonalidad en los polinomios")
        nText1.move_to(DOWN*1)

        self.play(Write(nText), Write(nText1), run_time=3)
        self.wait(2)
        self.play(FadeOut(nText), FadeOut(nText1))
        self.wait(4)

        leg1 = MathTex("P_0 (x) = 1")
        leg2 = MathTex("P_1 (x) = x")
        leg3 = MathTex("P_2 (x) = \\frac{1}{2} (3 x^2 - 1)")
        leg1.move_to(UP*1)
        leg3.move_to(DOWN*1)

        leg = Tex("Polinomios de Legendre")
        leg.move_to(UP*3)

        self.play(Write(leg1), Write(leg2), Write(leg3), run_time=2)
        self.play(Write(leg))
        self.wait(1)
        self.play(FadeOut(leg))
        self.play(leg1.animate.move_to(UP*1 + LEFT*5).scale(0.5), leg2.animate.move_to(LEFT*5).scale(0.5), leg3.animate.move_to(DOWN*1 + LEFT*5).scale(0.5))

        ax = Axes(
            x_range=[-1, 1.01, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={
                "include_numbers": True,
                "numbers_to_include": np.arange(-1, 1.01, 2),
                "numbers_with_elongated_ticks": np.arange(-1, 1.01, 2),
            },
            tips=False,
        )
        ax.move_to(RIGHT * 2).scale(0.8)
        self.play(FadeIn(ax), run_time=2)

        pol1 = ax.plot(lambda x: 1, x_range=[-1, 1], color=BLUE)
        pol2 = ax.plot(lambda x: x, x_range=[-1, 1], color=GREEN)
        pol3 = ax.plot(lambda x: 1/2*3*x**2 -1, x_range=[-1, 1], color=RED)

        self.play(Create(pol1), Create(pol2), Create(pol3), run_time=4)
        self.wait(2)
        self.play(FadeOut(pol1), FadeOut(pol2), FadeOut(pol3), FadeOut(ax))
        leg1.set_color(BLUE)
        leg2.set_color(GREEN)
        leg3.set_color(RED)
        leg = VGroup(leg1, leg2, leg3)

        self.play(leg.animate.to_corner(UL),
                  run_time=2)

        peso = MathTex("\\langle P_n (x), P_m (x) \\rangle_w ")
        sea = Tex("Con n diferente de m")
        sea.move_to(DOWN*1)

        self.play(Write(peso), Write(sea), run_time=2)
        self.play(FadeOut(sea))

        eqq = MathTex(" \\langle P_n (x), P_m (x) \\rangle_w = \\int_{-1}^1 P_n (x) P_m (x) dx")
        self.play(TransformMatchingShapes(peso, eqq), run_time=2)
        self.wait(2)

        eqq2 = MathTex("\\int_{-1}^1 P_n (x) P_m (x) dx = \\int_{-1}^1 P_1 (x) P_2 (x) dx",)
        eqq3 = MathTex(
            "\\int_{-1}^1 P_1 (x) P_2 (x) dx = \\int_{-1}^1 x (\\frac{1}{2} (3 x^2 - 1)) dx",
            tex_to_color_map={
                "x": RED,
                "\\frac{1}{2} (3 x^2 - 1)": GREEN
            }
                       )
        eqq4 = MathTex("\\int_{-1}^1 x (\\frac{1}{2} (3 x^2 - 1)) dx = \\int_{-1}^1 \\frac{3}{2} x^3 - \\frac{1}{2} x dx",
                       tex_to_color_map={
                           "x": RED,
                           "\\frac{1}{2} (3 x^2 - 1)": GREEN
                       }
                       )
        eqq5 = MathTex("\\int_{-1}^1 \\frac{3}{2} x^3 - \\frac{1}{2} x dx = 0")


        self.play(TransformMatchingShapes(eqq, eqq2), run_time=2)
        self.wait(2)
        self.play(TransformMatchingShapes(eqq2, eqq3), run_time=2)
        self.wait(2)
        self.play(TransformMatchingShapes(eqq3, eqq4), run_time=2)
        self.wait(2)
        self.play(TransformMatchingShapes(eqq4, eqq5), run_time=2)
        self.wait(2)
        self.play(FadeOut(eqq5), run_time=2)
        self.wait(5)

        eqq5.move_to(UP*3).scale(0.6)
        self.play(Write(eqq5))
        ax.move_to(ORIGIN)
        nPol = ax.plot(lambda x: x/2*(3*x**2 - 1), x_range=[-1, 1], color=PURPLE)
        self.play(FadeIn(ax), run_time=2)
        self.play(Create(nPol), run_time=3)

        area1 = ax.get_area(nPol, [math.sqrt(3)/-3, 0], color=TEAL, opacity=0.7)
        area3 = ax.get_area(nPol, [-1, math.sqrt(3)/-3], color=RED, opacity=0.7)
        area2 = ax.get_area(nPol, [0, math.sqrt(3)/3], color=RED, opacity=0.7)
        area4 = ax.get_area(nPol, [math.sqrt(3)/3, 1], color=TEAL, opacity=0.7)

        areas = VGroup(area1, area2, area3, area4)

        self.play(FadeIn(area1), FadeIn(area2), FadeIn(area3), FadeIn(area4), run_time=3)
        self.wait(2)
        self.play(FadeOut(ax), FadeOut(nPol), run_time=2)
        self.wait(2)

        self.play(FadeOut(areas), run_time=3)
        self.wait(1)

        self.play(
            FadeOut(eqq5),
            FadeOut(leg1),
            FadeOut(leg2),
            FadeOut(leg3),
            run_time=3
        )
        self.wait(3)

        nLine = Line([-2, 0, 0], [2, 0, 0])
        nLine.move_to(UP)
        nDot = Dot(nLine.point_from_proportion(0.5), color=BLUE)

        sinFunc = ParametricFunction(
            lambda t: np.array([c_func4(t)[0], c_func4(t)[1], np.sin(12*t)*1/14]),
            color=BLUE
        )
        sinFunc.move_to(DOWN*1.1)

        self.play(Create(nLine), Create(nDot), Create(sinFunc), run_time=3)
        self.play(FadeOut(nLine, shift=DL), FadeOut(nDot, shift=DL), run_time=2)
        sinFunc2 = FunctionGraph(
            lambda t: np.cos(t**3) + np.sin(7*t)*1/2 + np.sin(14*t),
            color=BLUE
        )

        sinFunc2.scale(0.2)
        sinFunc2.move_to(UP*2 + LEFT*5)
        framebox1 = SurroundingRectangle(sinFunc2, buff=.1, color=GRAY)
        self.play(ReplacementTransform(sinFunc, sinFunc2), Create(framebox1), run_time=4)

        text = MathTex(r"f(x) = cos(x^3) +"+ "\\frac{sin(7 x)}{2} +" +"\\frac{sin(14 x)}{7}")

        self.play(Write(text), run_time=3)
        self.wait(5)

        nText1 = Tex("Mínimos Cuadrados")

        self.play(
            sinFunc2.animate.move_to(UP*3 + LEFT*5),
            framebox1.animate.move_to(UP*3 + LEFT*5),
            text.animate.move_to(UP*3).scale(0.8),
            Write(nText1, run_time=2)
        )
        self.play(FadeOut(nText1))

        formulita = MathTex("Error = \\int_{-1}^{1} [f(x) - P(x)]^2 dx")

        formulita1 = MathTex("a_0 \\int_{-1}^{1} x^0 dx +a_1 \\int_{-1}^{1} x^1 dx + a_2 \\int_{-1}^{1} x^2 dx ="
                             +"\\int_{-1}^{1} cos(x^3) +"
                             + "\\frac{sin(7 x)}{2} +"
                             +"\\frac{sin(14 x)}{7} dx")

        formulita2 = MathTex("a_0 \\int_{-1}^{1} x^1 dx +a_1 \\int_{-1}^{1} x^2 dx + a_2 \\int_{-1}^{1} x^3 dx ="
                             +"\\int_{-1}^{1} x(cos(x^3) +"
                             + "\\frac{sin(7 x)}{2} +"
                             +"\\frac{sin(14 x)}{7}) dx")

        formulita3 = MathTex("a_0 \\int_{-1}^{1} x^2 dx +a_1 \\int_{-1}^{1} x^3 dx + a_2 \\int_{-1}^{1} x^4 dx ="
                             + "\\int_{-1}^{1} x^2(cos(x^3) +"
                             + "\\frac{sin(7 x)}{2} +"
                             + "\\frac{sin(14 x)}{7}) dx")
        formulita1.move_to(formulita2.get_center() + UP*1).scale(0.5)
        formulita2.scale(0.5)
        formulita3.move_to(formulita2.get_center() + DOWN*1).scale(0.5)


        sistema = VGroup(formulita1, formulita2, formulita3)

        braces = Brace(sistema, LEFT)

        self.play(Write(formulita), run_time=2)
        self.wait(2)
        self.play(FadeOut(formulita), run_time=2)
        self.wait(1)
        self.play(Write(sistema), GrowFromCenter(braces), run_time=5)
        self.wait(7)
        self.play(FadeOut(sistema), FadeOut(braces), run_time=2)
        self.wait(3)

        poli = MathTex("P(x) = a_0 \\varphi_0 (x) +"
                       +"a_1 \\varphi_1 (x) +"
                       +"\\cdot \\cdot \\cdot + a_n \\varphi_n (x)")
        poli.move_to(UP*1)

        poli2 = MathTex("P(x) = a_0 \\varphi_0 (x) +"
                       + "a_1 \\varphi_1 (x) +"
                       + "\\cdot \\cdot \\cdot + a_n \\varphi_n (x)")
        poli2.move_to(UP * 1)

        ortoTex = MathTex("\\{\\varphi_0 ; \\varphi_1; ....; \\varphi_n\\}: \\langle P_n (x), P_m (x) \\rangle_w = 0")

        self.play(Write(poli), run_time=2)
        self.wait(6)
        self.play(TransformMatchingShapes(poli2, ortoTex), run_time=2)
        self.wait(6)
        self.play(FadeOut(poli), FadeOut(ortoTex))
        self.wait(3)

        npoli = MathTex("a_0 \\int_{-1}^{1} \\varphi_{0}^{2} (x) dx +", "a_1\\int_{-1}^{1} \\varphi_{1} (x) \\varphi_0 (x) dx", "+", "a_2 \\int_{-1}^{1} \\varphi_2 (x) \\varphi_0 (x) dx", "="
                             +"\\int_{-1}^{1} cos(x^3) +"
                             + "\\frac{sin(7 x)}{2} +"
                             +"\\frac{sin(14 x)}{7} \\varphi_0 (x) dx")
        npoli.scale(0.4)
        frame_1 = SurroundingRectangle(npoli[1], buff=.1)
        frame_2 = SurroundingRectangle(npoli[3], buff=.1)

        self.play(Write(npoli), run_time=3)
        self.wait(6)
        self.play(Create(frame_1), Create(frame_2), run_time=2)
        self.wait(10)

        arrow1 = Line(start=frame_1.get_corner(DL), end=frame_1.get_corner(UR), color=PURE_RED)
        arrow2 = Line(start=frame_2.get_corner(DL), end=frame_2.get_corner(UR), color=PURE_RED)
        cerito1 = Tex("0")
        cerito1.scale(0.5)
        cerito2 = cerito1.copy()

        cerito1.move_to(arrow1.get_end()+UP*0.5)
        cerito2.move_to(arrow2.get_end()+UP*0.5)

        self.play(Create(arrow1), Create(arrow2))
        self.play(Write(cerito1), Write(cerito2))
        self.wait(12)

        self.play(
            FadeOut(cerito1),
            FadeOut(cerito2),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(frame_1),
            FadeOut(frame_2),
            FadeOut(npoli),
            run_time=4
        )
        self.wait(3)

        self.play(Uncreate(framebox1), text.animate.scale(0.7))

        axes = Axes(
            x_range=[-4.5, 4.5],
            y_range=[-4, 7],
            x_axis_config={"numbers_to_include": [-10.5, 1]},
            y_axis_config={"numbers_to_include": [-10.5, 1]},
            axis_config={"stroke_width": 2},
        )

        obj1 = axes.plot(lambda t: np.cos(t**3) + np.sin(7*t)*1/2 + np.sin(14*t), x_range=[-4, 4], color=BLUE)

        self.play(Transform(sinFunc2, obj1), Uncreate(framebox1), run_time=3)
        self.wait(3)

        approx_1= axes.plot(lambda t: -0.00005304638405219609*t**(10)-0.0006374842891224792 *t**(8)-0.014564153719024636*t**(6)+0.1232158749013575*t**(4)-0.0009374497203082388*t**(2)+0.5000016325062023 *np.sin(7 *t)+0.2500004569778431*np.sin(14*t)+0.4837643525992674*np.cos(t**(3)), color=YELLOW)
        approx_2= axes.plot(lambda t: 0.000018758774740680524*t**(11)-0.00007022507719155416*t**(9)-0.0011108308710159375*t**(7)+0.018483029527657817*t**(5)-0.0002064919092509431*t**(3)+0.0001062657123751182*t+0.4999995099906975*np.sin(7*t)+0.2499992440023417*np.sin(14*t)+0.4843603565451217*np.cos(t**(3)), color=PURE_RED)
        approx_3= axes.plot(lambda t: -0.000004969725663367179*t**(12)+0.000022580122307317294*t**(10)+0.0003464894873601185*t**(8)-0.006400479965166644*t**(6)+0.06604803214756637*t**(4)-0.0003703378170687177*t**(2)+0.49999984337592126*np.sin(7*t)+0.25000010246412774*np.sin(14*t)+0.48394324343489105*np.cos(t**(3)), color= PURE_GREEN)

        self.play(Create(approx_1), run_time=3)
        self.wait(3)
        self.play(Create(approx_2), run_time=3)
        self.wait(3)
        self.play(Create(approx_3), run_time=3)
        self.wait(3)

        self.play(FadeOut(sinFunc2), FadeOut(approx_1), FadeOut(approx_2), FadeOut(approx_3), FadeOut(text), run_time=6)
        self.wait(7)

        mob = Circle(radius=4, color=TEAL_A)
        text = Tex("Vamos un poco más atrás...", color=TEAL_A)
        self.play(Broadcast(mob), GrowFromCenter(text), run_time=8)
        self.wait(1)
        self.play(text.animate.scale(200), run_time=3)
        self.wait(1)
        self.play(FadeOut(text), run_time=2)

        legendre = ImageMobject("Legendre.jpg")
        legendre.to_corner(UL)
        self.play(FadeIn(legendre), run_time=2)
        self.wait(3)

        year = Tex("1782")
        year.to_corner(UR)

        self.play(Write(year), run_time=2)
        self.wait(2)

        earth = ImageMobject("earth.png")
        moon = ImageMobject("moon.png")
        earth.scale(0.3)
        moon.move_to(RIGHT*3).scale(0.1)

        arrow1 = Arrow(start=LEFT, end=RIGHT, color=PURE_RED)
        arrow2 = Arrow(start=LEFT, end=RIGHT, color=PURE_GREEN)
        arrow2.scale(0.5)

        arrow2.move_to(moon.get_center())

        traced_path = DashedVMobject(Circle(radius=3, color=YELLOW), num_dashes=43)
        self.play(GrowFromCenter(earth), GrowFromCenter(moon), run_time=2)
        self.play(Create(arrow1), Create(arrow2))
        self.play(
            Rotate(moon, angle=PI/2, about_point=ORIGIN, rate_func=linear),
            Rotate(arrow2, angle=PI/2, about_point=ORIGIN, rate_func=linear),
            Rotate(arrow1, angle=PI / 2, about_point=ORIGIN, rate_func=linear),
            Create(traced_path),
            run_time=6
        )

        self.play(
            Rotate(moon, angle=PI / 2, about_point=ORIGIN, rate_func=linear),
            Rotate(arrow2, angle=PI / 2, about_point=ORIGIN, rate_func=linear),
            Rotate(arrow1, angle=PI / 2, about_point=ORIGIN, rate_func=linear),
            FadeOut(moon),
            FadeOut(earth),
            FadeOut(arrow2),
            FadeOut(arrow1),
            FadeOut(traced_path),
            FadeOut(legendre),
            FadeOut(year)
        )
        self.wait(3)
        gregory = ImageMobject("Gregory.jpeg")

        gregory.to_corner(UL)

        century = Tex("1668")
        century.to_corner(UR)

        self.play(FadeIn(gregory), Write(century))
        self.wait(3)
        titulo = Tex("Geometriae Pars Universalis")
        subtitulo = Tex("Proposición 47")

        titulo.scale(0.7).move_to(UP * 2)
        subtitulo.scale(0.5).move_to(UP * 1)

        self.play(Write(titulo), run_time=3)
        self.play(Write(subtitulo), run_time=3)
        self.wait(3)
        self.play(FadeOut(titulo))
        self.play(FadeOut(subtitulo))

        # Definir la función paramétrica para la elipse
        a = 4  # Semieje mayor
        b = 2  # Semieje menor
        ellipse_func = lambda t: np.array([a * np.cos(t), b * np.sin(t), 0])

        # Crear la instancia de ParametricFunction
        ellipse = ParametricFunction(ellipse_func, t_range=(0, np.pi), color=PURE_RED)

        # Agregar la elipse a la escena
        self.play(Create(ellipse))

        # Agregar los ejes
        axes = Axes(
            x_range=[-4.5, 4.5],
            y_range=[-3, 3],
            x_axis_config={"numbers_to_include": [-4, 4]},
            y_axis_config={"numbers_to_include": [-2, 2]},
            axis_config={"stroke_width": 2},
        )
        self.play(FadeIn(axes))

        self.play(
            FadeOut(axes),
            FadeOut(ellipse),
            FadeOut(gregory),
            FadeOut(year),
            run_time=8
        )
