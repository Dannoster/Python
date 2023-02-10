import numpy as np
from matplotlib import pyplot as plt
import os
np.seterr(divide = 'ignore') 



class _Particle:


    SIGNS = (-1, 1)

    def __init__(self, volume, p0=1, mass=1, x=None, y=None, z=None, px=None, py=None, pz=None):
       
        self._mass = mass
        self.was_collided = False

        if px == None or py == None or pz == None:
            self.new_direction(p0)
        else:
            self.px = px
            self.py = py
            self.pz = pz

        if x == None or y == None or z == None:
            self.x = np.random.rand() * volume.a
            self.y = np.random.rand() * volume.b
            self.z = np.random.rand() * volume.c
        else:
            self.x = x
            self.y = y
            self.z = z

    def new_direction(self, abs_p):
        random_values = np.random.rand(3)
        koeff = abs_p / np.sqrt(random_values[0]**2 + random_values[1]**2 + random_values[2]**2) # нормировка
        self.px, self.py, self.pz = koeff*random_values
        self.px *= np.random.choice(_Particle.SIGNS)
        self.py *= np.random.choice(_Particle.SIGNS)
        self.pz *= np.random.choice(_Particle.SIGNS)

    @property
    def mass(self):
        return self._mass


class _Center(_Particle):


    def __init__(self, volume, p0=10000, mass=100000, x=None, y=None, z=None, px=10000, py=0, pz=0, is_left=True, sigma=0.5):
        super().__init__(volume, p0, mass, x, y, z, px, py, pz)
        self.is_left = is_left
        self.sigma = sigma
        if is_left:
            self.x /= 2
            self.px *= sigma
        else:
            self.x = (volume.a + self.x)/2
        self.diameter = 0.1 * np.sqrt(volume.a**2 + volume.b**2 + volume.c**2)
        if px == None or py == None or pz == None:
            self.px = 10000 + 10000*0.15*np.random.random() * np.random.choice(_Particle.SIGNS)
            self.py = 10000*0.15*np.random.random() * np.random.choice(_Particle.SIGNS)
            self.pz = 10000*0.15*np.random.random() * np.random.choice(_Particle.SIGNS)


class Volume:


    def __init__(self, a=1000, b=1000, c=1000,
            number_of_particles=1000, delta_p=0.2, disp_probability=0.01):
        self._a = a
        self._b = b
        self._c = c
        self._delta_p = delta_p
        self._disp_probability = disp_probability
        self._particles = []
        for _ in range(number_of_particles):
            self._particles.append(_Particle(self))
        self.dir_name = "1_simple_volume"

    def start_modeling(self, seconds=10000, visualisation_step=600):
        for i in range(seconds+1):
            # print(self._particles[0].x,"\t",self._particles[0].px)
            if i%visualisation_step == 0:
                self._save(sec=i)
            for particle in self._particles:
                self._check_particle(particle)

    def _check_particle(self, particle):
        self._check_random_dispersion(particle)
        self._check_x_axis(particle)
        self._check_y_axis(particle)
        self._check_z_axis(particle)

    def _check_random_dispersion(self, particle: _Particle):
        if np.random.rand() <= self._disp_probability:
            self._change_direction(particle)
            
    def _change_direction(self, particle: _Particle):
        current_impulse = np.sqrt(particle.px**2 + particle.py**2 + particle.pz**2)
        particle.new_direction(current_impulse)

    def _check_x_axis(self, particle: _Particle):
        if particle.x + particle.px / particle.mass - self.a/2 \
                <= particle.px / particle.mass:
            particle.px += self._delta_p
            particle.x += particle.px / particle.mass
        elif particle.x + particle.px / particle.mass > self.a:
            particle.x = self.a
            particle.px *= -1
        elif particle.x + particle.px / particle.mass < 0:
            particle.x = 0
            particle.px *= -1
        else:
            particle.x += particle.px / particle.mass

    def _check_y_axis(self, particle: _Particle):
        if particle.y + particle.py / particle.mass > self.b:
            particle.y = self.b
            particle.py *= -1
        elif particle.y + particle.py / particle.mass < 0:
            particle.y = 0
            particle.py *= -1
        else:
            particle.y += particle.py / particle.mass

    def _check_z_axis(self, particle: _Particle):
        if particle.z + particle.pz / particle.mass > self.c:
            particle.z = self.c
            particle.pz *= -1
        elif particle.z + particle.pz / particle.mass < 0:
            particle.z = 0
            particle.pz *= -1
        else:
            particle.z += particle.pz / particle.mass

    def _save(self, sec):
        p_array = [np.sqrt(particle.px**2 + particle.py**2 + particle.pz**2) for particle in self._particles]
        # print(p_array)
        fig, ax = plt.subplots()
        ax.set_axisbelow(True)
        plt.title(rf"Impulse distribution after {sec//60} minutes, {len(self._particles)} particles, $p_0=1$")
        plt.xlabel(r"$p/p_0$")
        plt.ylabel("N")
        plt.xscale("log")
        plt.yscale("log")
        plt.grid(which='both', linestyle=':')
        log_bins = 1.5**(np.arange(0,16)-1)   # log_bins = np.logspace(0, 3, num=16) 
        bin_centers = np.array([(log_bins[i] + log_bins[i+1])/2 for i in range(len(log_bins)-1)])
        n, bins, patches = plt.hist(p_array, bins=log_bins, rwidth=0.9)
        n = np.array(n)
        bin_centers = np.array([(bins[i] + bins[i+1])/2 for i in range(len(bins)-1)])
        log_n = np.log10(n)
        log_bin_centers = np.log10(bin_centers)
        # print(len(self._particles), sum(n))
        log_bin_centers = log_bin_centers[log_n != float('-inf')]
        log_n = log_n[log_n != float('-inf')]
        fit = np.polyfit(log_bin_centers, log_n, 1)
        k = fit[0]
        y0 = fit[1]
        if sec != 0:
            plt.plot(np.power(10, log_bin_centers), np.power(10, y0 + k*log_bin_centers), 
                label=rf"$k={k:.02f}$")
            plt.legend()
        self._make_dir()
        plt.savefig(f"{self.dir_name}/dist{sec//60}")
        plt.cla()
        plt.clf()
        plt.close()
        
    def _make_dir(self):
        try:
            os.mkdir(self.dir_name)
        except FileExistsError:
            pass
        
    @property
    def a(self):
        return self._a
    @property
    def b(self):
        return self._b
    @property
    def c(self):
        return self._c



class LeftOpenedVolume(Volume):

    def __init__(self, a=1000, b=1000, c=1000, number_of_particles=1000, delta_p=0.2, disp_probability=0.01, left_leave_probability=0.8):
        super().__init__(a, b, c, number_of_particles, delta_p, disp_probability)
        self._left_leave_probability = left_leave_probability
        self.dir_name = "2_left_opened_volume"

    def _check_x_axis(self, particle: _Particle):
        if particle.x + particle.px / particle.mass - self.a/2 \
                <= particle.px / particle.mass:
            particle.px += self._delta_p
            particle.x += particle.px / particle.mass
        elif particle.x + particle.px / particle.mass > self.a:
            particle.x = self.a
            particle.px *= -1
        elif particle.x + particle.px / particle.mass < 0:
            if np.random.random <= self._left_leave_probability:
                new_particle = _Particle(self)
                particle.x = new_particle.x
                particle.y = new_particle.y
                particle.z = new_particle.z
                particle.px = new_particle.px
                particle.py = new_particle.py
                particle.pz = new_particle.pz
            else:
                particle.x = 0
                particle.px *= -1
        else:
            particle.x += particle.px / particle.mass


class VolumeWithCenters(Volume):
   
   
    def __init__(self, a=1000, b=1000, c=1000, number_of_particles=1000, delta_p=0.2, 
            disp_probability=0.01, number_of_centers=None, sigma=0.5):
        super().__init__(a, b, c, number_of_particles, delta_p, disp_probability)
        self._sigma = sigma
        self._centers = []
        if number_of_centers == None:
            number_of_centers = number_of_particles // 10
        for i in range(int(number_of_centers)):
            if i < number_of_centers/(1 + sigma):
                self._centers.append(_Center(self, is_left=True))
            else:
                self._centers.append(_Center(self, is_left=False))
        self.dir_name = "3_volume_with_centers"

    def start_modeling(self, seconds=10000, visualisation_step=600):
        super().start_modeling(seconds, visualisation_step)
        for center in self._centers:
            self._check_center(center)

    def _check_particle(self, particle: _Particle):
        super()._check_particle(particle)
        self._check_particle_collisions(particle)
        particle.was_collided = False

    def _check_particle_collisions(self, particle: _Particle):
        for center in self._centers:
            near_center = \
                center.x <= particle.x <= (center.x + center.diameter) and \
                center.y <= particle.y <= (center.y + center.diameter) and \
                center.z <= particle.z <= (center.z + center.diameter)
            if not particle.was_collided and near_center:
                self._change_direction(particle)
                particle.was_collided = True

    def _check_center(self, center: _Center):
        if center.is_left:
            left_x = 0
            right_x = self.a/2
        else:
            left_x = self.a/2
            right_x = self.a 

        if not (left_x <= center.x <= right_x) or \
                not (0 <= center.x <= self.b) or \
                not (0 <= center.x <= self.c):
            self._create_new(center)
        else:
            center.x += center.px / center.mass
            center.y += center.py / center.mass
            center.z += center.pz / center.mass

    def _create_new(self, center: _Center):
        new_center = _Center(self, is_left=center.is_left)
        center.x = new_center.x
        center.y = new_center.y
        center.z = new_center.z
        center.px = new_center.px
        center.py = new_center.py
        center.pz = new_center.pz


class VolumeWithRandomCenters(VolumeWithCenters):   # same but with Nones in _Center()


    def __init__(self, a=1000, b=1000, c=1000, number_of_particles=1000, delta_p=0.2, 
            disp_probability=0.01, number_of_centers=None, sigma=0.5):
        super().__init__(a, b, c, number_of_particles, delta_p, disp_probability)
        self._sigma = sigma
        self._centers = []
        if number_of_centers == None:
            number_of_centers = number_of_particles // 10
        for i in range(number_of_centers):
            if i < number_of_centers/(1 + sigma):
                self._centers.append(_Center(self, is_left=True, px=None, py=None, pz=None))
            else:
                self._centers.append(_Center(self, is_left=False, px=None, py=None, pz=None))
        self.dir_name = "4_volume_with_random_centers"

    def _create_new(self, center: _Center):
        new_center = _Center(self, is_left=center.is_left, px=None, py=None, pz=None)
        center.x = new_center.x
        center.y = new_center.y
        center.z = new_center.z
        center.px = new_center.px
        center.py = new_center.py
        center.pz = new_center.pz


class LeftOpenedVolumeWithRandomCenters(VolumeWithCenters, LeftOpenedVolume):

    def __init__(self, a=1000, b=1000, c=1000, number_of_particles=1000, delta_p=0.2, disp_probability=0.01, left_leave_probability=0.8, number_of_centers=None, sigma=0.5):
        super().__init__(a, b, c, number_of_particles, delta_p, disp_probability, number_of_centers, sigma)
        self._left_leave_probability = left_leave_probability
        self.dir_name = "5_left_opened_volume_with_random_centers"


class UltimateVolumeWithEnergyLoss(LeftOpenedVolumeWithRandomCenters):
    

    def __init__(self, a=1000, b=1000, c=1000, number_of_particles=1000, delta_p=0.2, \
            disp_probability=0.01, number_of_centers=None, sigma=0.5, energy_loss=0.05):
        super().__init__(a, b, c, number_of_particles, delta_p, disp_probability, number_of_centers, sigma)
        self._energy_loss = energy_loss
        self.dir_name = "6_volume_with_energy loss"

    def _check_particle(self, particle: _Particle):
        super()._check_particle(particle)
        self._check_energy_loss(particle)

    def _check_energy_loss(self, particle: _Particle):
        if particle.x >= self.a:
            current_impulse = np.sqrt(particle.px**2 + particle.py**2 + particle.pz**2)
            if current_impulse > self._energy_loss:
                koeff = 1 - self._energy_loss / current_impulse
                particle.px *= koeff
                particle.py *= koeff
                particle.pz *= koeff
            else:
                particle.px *= 1e-10
                particle.py *= 1e-10
                particle.pz *= 1e-10

if __name__ == "__main__":
    print("\n\nИмпортируйте этот файл как модуль, например, так:\nimport particles as prt\n")