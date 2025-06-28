package com.mycompany.pruebaexcepcionesui;

public class Operaciones {
    public static double division(double numerador, double denominador) {
        try {
            return numerador/denominador;
        }
    
        catch (ArithmeticException e) {
            return 0;
        }
        catch (Exception e) {
            return -1;
        }
    }
}