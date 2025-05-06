class Ball
{
    public:
    Ball(std::array<double, 3> p, double r, double m);
    
    std::array<double, 3> position;
    double getRadius(){return radius;}
    double getMass(){return mass;}
    double getDensity(){return density;}

    private:
    void setDensity();

    double radius;
    double mass;
    double density;
};
