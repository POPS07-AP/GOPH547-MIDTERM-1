#GOPH 547 - Midterm Exam Solutions
#Course: Gravity Theory I

- Part I: Multiple Choice (answers only)
- Part II: Vector Operations and Curvilinear Coordinates
- Part III: Gravitational Flux and Equivalent Surface Density
- Part IV: Theoretical Gravity / Rotating Frame
"""

import numpy as np
from typing import Dict, Tuple

# ============================================================================
# CONSTANTS
# ============================================================================

G = 6.67430e-11  # Gravitational constant [m^3 kg^-1 s^-2]
M_earth = 5.972e24  # Earth mass [kg]
R_earth = 6371000  # Earth mean radius [m]
R_equator = 6378137  # Earth equatorial radius [m]
f = 1 / 298.257  # Earth flattening factor
omega_earth = 7.292115e-5  # Earth rotation rate [rad/s]


# ============================================================================
# PART I - MULTIPLE CHOICE ANSWERS
# ============================================================================

def part_i_answers():
    """Print answers for multiple choice questions 1-10."""

    print("=" * 60)
    print("PART I - MULTIPLE CHOICE ANSWERS")
    print("=" * 60)

    answers = {
        1: "b) There is a net influx",
        2: "a and d",
        3: "a, b, and c",
        4: "a and b",
        5: "b, c, and d",
        6: "d) A direction in the xz-plane",
        7: "b and d",
        8: "a",
        9: "-GMx/r³",
        10: "b and d"
    }

    for i in range(1, 11):
        print(f"Question {i:2d}: {answers[i]}")

    print("=" * 60)


# ============================================================================
# PART II - VECTOR OPERATIONS AND CURVILINEAR COORDINATES
# ============================================================================

def part_ii_solution():
    """
    Part II: Vector Operations and Curvilinear Coordinates

    Given:
    M = 8.681e25 kg
    Point P: {x,y,z} = {55.0e6, 55.0e6, 32.5e6} m
    G = 6.67430e-11 m³ kg⁻¹ s⁻²
    """

    print("\n" + "=" * 80)
    print("PART II - VECTOR OPERATIONS AND CURVILINEAR COORDINATES")
    print("=" * 80)

    # Given values
    M = 8.681e25
    x, y, z = 55.0e6, 55.0e6, 32.5e6

    print(f"\nGiven:")
    print(f"  M = {M:.3e} kg")
    print(f"  Point P: ({x / 1e6:.1f}, {y / 1e6:.1f}, {z / 1e6:.1f}) × 10⁶ m")
    print(f"  G = {G:.3e} m³ kg⁻¹ s⁻²")

    # =========================================================
    # Part II(a): Gravitational field components
    # =========================================================

    print("\n" + "-" * 60)
    print("Part II(a) - Gravitational Field Components")
    print("-" * 60)

    # Step 1: Calculate distance r
    r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
    r2 = r ** 2
    r3 = r ** 3

    print(f"\nStep 1: Calculate distance r")
    print(f"  r = √(x² + y² + z²)")
    print(f"  r = √(({x / 1e6:.1f})² + ({y / 1e6:.1f})² + ({z / 1e6:.1f})²) × 10⁶")
    print(f"  r² = (3025 + 3025 + 1056.25) × 10¹² = 7106.25 × 10¹² m²")
    print(f"  r = √(7106.25) × 10⁶ = {r / 1e6:.3f} × 10⁶ m = {r:.3e} m")

    # Step 2: Calculate GM
    GM = G * M
    print(f"\nStep 2: Calculate GM")
    print(f"  GM = G × M")
    print(f"  GM = ({G:.3e}) × ({M:.3e}) = {GM:.3e} m³/s²")

    # Step 3: Derive g_x, g_y, g_z
    print(f"\nStep 3: Derive g_x, g_y, g_z")
    print(f"  U = -GM/r = -GM(x² + y² + z²)⁻¹/²")
    print(f"  ∂U/∂x = -GM · (-1/2)(x² + y² + z²)⁻³/² · (2x) = GMx/r³")
    print(f"  Similarly: ∂U/∂y = GMy/r³, ∂U/∂z = GMz/r³")
    print(f"  g = -∇U, so:")
    print(f"  g_x = -∂U/∂x = -GMx/r³")
    print(f"  g_y = -∂U/∂y = -GMy/r³")
    print(f"  g_z = -∂U/∂z = -GMz/r³")

    # Step 4: Calculate components
    common_factor = -GM / r3
    g_x = common_factor * x
    g_y = common_factor * y
    g_z = common_factor * z

    print(f"\nStep 4: Calculate components")
    print(f"  Common factor = -GM/r³ = {common_factor:.3e} s⁻²")
    print(f"  g_x = ({common_factor:.3e}) × ({x:.3e}) = {g_x:.4f} m/s²")
    print(f"  g_y = ({common_factor:.3e}) × ({y:.3e}) = {g_y:.4f} m/s²")
    print(f"  g_z = ({common_factor:.3e}) × ({z:.3e}) = {g_z:.4f} m/s²")

    # Step 5: Calculate magnitude
    g_mag = np.sqrt(g_x ** 2 + g_y ** 2 + g_z ** 2)
    print(f"\nStep 5: Calculate magnitude ||g||")
    print(f"  ||g|| = √(g_x² + g_y² + g_z²)")
    print(f"  ||g|| = √({g_x:.4f}² + {g_y:.4f}² + {g_z:.4f}²)")
    print(f"  ||g|| = √({g_x ** 2:.4f} + {g_y ** 2:.4f} + {g_z ** 2:.4f})")
    print(f"  ||g|| = √{g_x ** 2 + g_y ** 2 + g_z ** 2:.4f} = {g_mag:.4f} m/s²")

    # Step 6: Calculate radial component
    g_r = -GM / r ** 2
    print(f"\nStep 6: Calculate radial component g_r")
    print(f"  g_r = g · r̂ = (-GM/r³)(xî + yĵ + zk̂) · (xî + yĵ + zk̂)/r")
    print(f"  g_r = -GM(x² + y² + z²)/r⁴ = -GM r²/r⁴ = -GM/r²")
    print(f"  g_r = -({GM:.3e})/({r:.3e})²")
    print(f"  g_r = -({GM:.3e})/({r ** 2:.3e}) = {g_r:.4f} m/s²")

    # =========================================================
    # Part II(b): Divergence and flux
    # =========================================================

    print("\n" + "-" * 60)
    print("Part II(b) - Divergence and Gravitational Flux")
    print("-" * 60)

    R_sphere = 75.0e6

    print(f"\nStep 1: Calculate divergence ∇·g")
    print(f"  ∇·g = ∂g_x/∂x + ∂g_y/∂y + ∂g_z/∂z")
    print(f"  g_x = -GMx(x² + y² + z²)⁻³/²")
    print(f"  ∂g_x/∂x = -GM[(1)(x²+y²+z²)⁻³/² + x·(-3/2)(x²+y²+z²)⁻⁵/²·(2x)]")
    print(f"  ∂g_x/∂x = -GM[1/r³ - 3x²/r⁵]")
    print(f"  Similarly:")
    print(f"  ∂g_y/∂y = -GM[1/r³ - 3y²/r⁵]")
    print(f"  ∂g_z/∂z = -GM[1/r³ - 3z²/r⁵]")
    print(f"  Summing: ∇·g = -GM[3/r³ - 3(x²+y²+z²)/r⁵]")
    print(f"  ∇·g = -GM[3/r³ - 3r²/r⁵] = -GM[3/r³ - 3/r³] = 0")
    print(f"\n  ∇·g = 0 s⁻² (for points far from the mass)")

    print(f"\nStep 2: Calculate total flux through sphere of radius R = {R_sphere / 1e6:.1f}×10⁶ m")
    print(f"  Using divergence theorem: ∫∫_S g·n dS = ∫∫∫_V (∇·g) dV")
    print(f"  Using Poisson equation: ∇·g = -4πGρ")
    print(f"  ∫∫∫_V (∇·g) dV = ∫∫∫_V (-4πGρ) dV = -4πG M_enc")
    print(f"  Total flux = -4πG M")

    total_flux = -4 * np.pi * GM
    print(f"  Total flux = -4π({GM:.3e}) = {total_flux:.3e} m³/s²")
    print(f"  (Note: Result is independent of sphere radius - all mass enclosed)")

    # =========================================================
    # Part II(c): Latitudinal unit vector
    # =========================================================

    print("\n" + "-" * 60)
    print("Part II(c) - Latitudinal Unit Vector θ̂")
    print("-" * 60)

    # Step 1: Calculate spherical coordinates
    r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
    sin_theta = z / r
    theta_rad = np.arcsin(sin_theta)
    theta_deg = np.degrees(theta_rad)
    phi_rad = np.arctan2(y, x)
    phi_deg = np.degrees(phi_rad)

    print(f"\nStep 1: Calculate spherical coordinates")
    print(f"  r = √(x² + y² + z²) = {r / 1e6:.3f} × 10⁶ m")
    print(f"  θ = arcsin(z/r) = arcsin({z:.3e}/{r:.3e}) = {theta_deg:.2f}°")
    print(f"  φ = arctan(y/x) = arctan({y:.3e}/{x:.3e}) = {phi_deg:.2f}°")

    # Step 2: Derive expression for θ̂
    print(f"\nStep 2: Derive expression for θ̂")
    print(f"  Position vector: r = (r cos θ cos φ)î + (r cos θ sin φ)ĵ + (r sin θ)k̂")
    print(f"  ∂r/∂θ = (-r sin θ cos φ)î + (-r sin θ sin φ)ĵ + (r cos θ)k̂")
    print(f"  Scale factor h_θ = |∂r/∂θ| = r")
    print(f"  θ̂ = (1/h_θ)(∂r/∂θ) = (-sin θ cos φ)î + (-sin θ sin φ)ĵ + (cos θ)k̂")

    # Step 3: Calculate components
    cos_theta = np.cos(theta_rad)
    cos_phi = np.cos(phi_rad)
    sin_phi = np.sin(phi_rad)

    theta_hat_x = -sin_theta * cos_phi
    theta_hat_y = -sin_theta * sin_phi
    theta_hat_z = cos_theta

    print(f"\nStep 3: Calculate components at point P")
    print(f"  sin θ = {sin_theta:.4f}")
    print(f"  cos θ = {cos_theta:.4f}")
    print(f"  cos φ = {cos_phi:.4f}")
    print(f"  sin φ = {sin_phi:.4f}")
    print(f"  θ̂_x = -sin θ cos φ = -({sin_theta:.4f})×({cos_phi:.4f}) = {theta_hat_x:.4f}")
    print(f"  θ̂_y = -sin θ sin φ = -({sin_theta:.4f})×({sin_phi:.4f}) = {theta_hat_y:.4f}")
    print(f"  θ̂_z = cos θ = {theta_hat_z:.4f}")

    # Step 4: Verify unit magnitude
    mag = np.sqrt(theta_hat_x ** 2 + theta_hat_y ** 2 + theta_hat_z ** 2)
    print(f"\nStep 4: Verify unit magnitude")
    print(f"  |θ̂| = √({theta_hat_x:.4f}² + {theta_hat_y:.4f}² + {theta_hat_z:.4f}²)")
    print(f"  |θ̂| = √{theta_hat_x ** 2 + theta_hat_y ** 2 + theta_hat_z ** 2:.4f} = {mag:.4f} = 1")

    # Store results for summary
    ii_results = {
        'g_x': g_x, 'g_y': g_y, 'g_z': g_z,
        'g_mag': g_mag, 'g_r': g_r,
        'total_flux': total_flux,
        'theta_hat': (theta_hat_x, theta_hat_y, theta_hat_z)
    }

    return ii_results


# ============================================================================
# PART III - GRAVITATIONAL FLUX AND EQUIVALENT SURFACE DENSITY
# ============================================================================

def part_iii_solution():
    """
    Part III: Gravitational Flux and Equivalent Surface Density

    Given:
    m₁ = 8.54 × 10⁵ kg
    m₂ = 3.26 × 10⁶ kg
    m₃ = 5.21 × 10⁶ kg
    r = 270 m (radius of hemisphere)
    G = 6.67430 × 10⁻¹¹ m³ kg⁻¹ s⁻²
    """

    print("\n" + "=" * 80)
    print("PART III - GRAVITATIONAL FLUX AND EQUIVALENT SURFACE DENSITY")
    print("=" * 80)

    # Given values
    m1 = 8.54e5
    m2 = 3.26e6
    m3 = 5.21e6
    r = 270

    print(f"\nGiven:")
    print(f"  m₁ = {m1:.3e} kg")
    print(f"  m₂ = {m2:.3e} kg")
    print(f"  m₃ = {m3:.3e} kg")
    print(f"  r = {r} m (radius of hemisphere)")
    print(f"  G = {G:.3e} m³ kg⁻¹ s⁻²")

    # =========================================================
    # Part III(a): Expression for flux integral
    # =========================================================

    print("\n" + "-" * 60)
    print("Part III(a) - Expression for Flux Integral")
    print("-" * 60)

    print(f"""
    From Gauss's law: ∫∫_S g·n dS = -4πG M_enc

    For a closed hemispherical surface containing all three masses:

    M_enc = m₁ + m₂ + m₃

    Therefore:

    ∫∫_S g·n dS = -4πG(m₁ + m₂ + m₃)

    This result is independent of the positions of the masses and the
    radius r, as long as all masses are fully contained within the surface.
    """)

    # =========================================================
    # Part III(b): Numerical value of flux integral
    # =========================================================

    print("\n" + "-" * 60)
    print("Part III(b) - Numerical Value of Flux Integral")
    print("-" * 60)

    # Calculate total enclosed mass
    M_enc = m1 + m2 + m3
    print(f"\nStep 1: Calculate total enclosed mass")
    print(f"  M_enc = m₁ + m₂ + m₃")
    print(f"  M_enc = {m1:.3e} + {m2:.3e} + {m3:.3e}")
    print(f"  M_enc = {M_enc:.3e} kg")

    # Calculate flux
    flux = -4 * np.pi * G * M_enc
    print(f"\nStep 2: Calculate flux integral")
    print(f"  ∫∫_S g·n dS = -4πG M_enc")
    print(f"  = -4π({G:.3e})({M_enc:.3e})")
    print(f"  = -4π({G * M_enc:.3e})")
    print(f"  = {flux:.3e} m³/s²")

    # =========================================================
    # Part III(c): Equivalent surface density
    # =========================================================

    print("\n" + "-" * 60)
    print("Part III(c) - Equivalent Surface Density")
    print("-" * 60)

    # Calculate surface area of hemisphere
    A_hemisphere = 2 * np.pi * r ** 2  # curved part
    A_circle = np.pi * r ** 2  # flat part
    A_total = A_hemisphere + A_circle  # total = 3πr²

    print(f"\nStep 1: Calculate surface area of hemisphere")
    print(f"  Area of hemispherical portion: 2πr² = 2π({r})² = {A_hemisphere:.1f} m²")
    print(f"  Area of flat circular portion: πr² = π({r})² = {A_circle:.1f} m²")
    print(f"  Total surface area: A = 3πr² = 3π({r})² = {A_total:.1f} m²")

    # Calculate equivalent surface density
    rho_star = M_enc / A_total
    print(f"\nStep 2: Calculate equivalent surface density")
    print(f"  ρ* = M_enc / A")
    print(f"  ρ* = ({M_enc:.3e}) / ({A_total:.1f})")
    print(f"  ρ* = {rho_star:.2f} kg/m²")

    print(f"\nStep 3: Compare with actual density")
    print(f"  Equivalent surface density has units of kg/m² (mass per unit area)")
    print(f"  Actual density has units of kg/m³ (mass per unit volume)")
    print(f"  ρ* represents a hypothetical uniform layer on the surface S that")
    print(f"  would produce the same far-field gravitational effect as the actual")
    print(f"  buried masses. It does not give information about the true density")
    print(f"  distribution inside the volume.")

    iii_results = {
        'M_enc': M_enc,
        'flux': flux,
        'rho_star': rho_star
    }

    return iii_results


# ============================================================================
# PART IV - THEORETICAL GRAVITY / ROTATING FRAME
# ============================================================================

def part_iv_solution():
    """
    Part IV: Theoretical Gravity / Rotating Frame

    Given:
    Latitude θ = 25.05° N
    Rotation period T = 23.93 hours
    a_c = 6,378,137 m (equatorial radius)
    f = 1/298.257 (flattening)
    G = 6.67430e-11 m³ kg⁻¹ s⁻²
    M = 5.972e24 kg (Earth mass)
    """

    print("\n" + "=" * 80)
    print("PART IV - THEORETICAL GRAVITY / ROTATING FRAME")
    print("=" * 80)

    # Given values
    theta_deg = 25.05
    T_hours = 23.93
    a_c = 6378137
    f = 1 / 298.257
    M = 5.972e24

    print(f"\nGiven:")
    print(f"  Latitude θ = {theta_deg}° N")
    print(f"  Rotation period T = {T_hours} hours")
    print(f"  Equatorial radius a_c = {a_c} m")
    print(f"  Flattening f = 1/298.257 = {f:.7f}")
    print(f"  G = {G:.3e} m³ kg⁻¹ s⁻²")
    print(f"  Earth mass M = {M:.3e} kg")

    # =========================================================
    # Part IV(a): Derive theoretical gravity expression
    # =========================================================

    print("\n" + "-" * 60)
    print("Part IV(a) - Derivation of Theoretical Gravity Expression")
    print("-" * 60)

    print(f"""
    In a rotating reference frame, the equation of motion is:

    a_fixed = a_rotating + a_Coriolis + a_centrifugal + a_Euler

    For an object at rest on Earth's surface (v_r = 0):
    - Coriolis term (-2Ω × v_r) = 0
    - Euler term (-(dΩ/dt) × r) = 0 (Earth's rotation is constant)

    The acceleration in the inertial frame is due to gravitational attraction:
    a_fixed = g_grav = -∇U

    In the rotating frame, the apparent acceleration (measured gravity) is:
    g_measured = g_grav + a_centrifugal

    The centrifugal acceleration is:
    a_centrifugal = -Ω × (Ω × r)

    For a point at latitude θ, the distance from the rotation axis is r cos θ,
    and the centrifugal acceleration is directed outward. Its radial component is:

    a_centrifugal,radial = Ω² r cos² θ

    Therefore, theoretical gravity at latitude θ is:

    g_theoretical(θ) = |g_grav| - Ω² r(θ) cos² θ

    where |g_grav| = GM/r(θ)² and r(θ) is the distance from Earth's centre
    to the surface at latitude θ.

    g_theoretical(θ) = GM/r(θ)² - Ω² r(θ) cos² θ
    """)

    # =========================================================
    # Part IV(b): Calculate theoretical gravity
    # =========================================================

    print("\n" + "-" * 60)
    print("Part IV(b) - Numerical Calculation of Theoretical Gravity")
    print("-" * 60)

    # Step 1: Calculate Earth's rotation rate
    T_sec = T_hours * 3600
    Omega = 2 * np.pi / T_sec
    print(f"\nStep 1: Calculate Earth's rotation rate Ω")
    print(f"  T = {T_hours} hours = {T_sec:.0f} s")
    print(f"  Ω = 2π/T = 2π/{T_sec:.0f} = {Omega:.4e} rad/s")

    # Step 2: Calculate radius at latitude θ
    theta_rad = np.radians(theta_deg)
    sin_theta = np.sin(theta_rad)
    sin2_theta = sin_theta ** 2
    r_theta = a_c * (1 - f * sin2_theta)
    print(f"\nStep 2: Calculate radius at latitude {theta_deg}°")
    print(f"  θ = {theta_deg}° = {theta_rad:.4f} rad")
    print(f"  sin θ = {sin_theta:.4f}")
    print(f"  sin² θ = {sin2_theta:.4f}")
    print(f"  r(θ) = a_c(1 - f sin² θ)")
    print(f"  r(θ) = {a_c}(1 - {f:.7f} × {sin2_theta:.4f})")
    print(f"  r(θ) = {a_c}(1 - {f * sin2_theta:.7f})")
    print(f"  r(θ) = {a_c} × {1 - f * sin2_theta:.7f}")
    print(f"  r(θ) = {r_theta:.0f} m")

    # Step 3: Calculate gravitational term GM/r²
    GM = G * M
    g_grav = GM / r_theta ** 2
    print(f"\nStep 3: Calculate gravitational term GM/r²")
    print(f"  GM = ({G:.3e}) × ({M:.3e}) = {GM:.4e} m³/s²")
    print(f"  g_grav = GM/r(θ)² = {GM:.4e}/({r_theta:.0f})²")
    print(f"  g_grav = {GM:.4e}/{r_theta ** 2:.4e} = {g_grav:.4f} m/s²")

    # Step 4: Calculate centrifugal term Ω² r cos² θ
    cos_theta = np.cos(theta_rad)
    cos2_theta = cos_theta ** 2
    centrifugal = Omega ** 2 * r_theta * cos2_theta
    print(f"\nStep 4: Calculate centrifugal term Ω² r cos² θ")
    print(f"  cos θ = {cos_theta:.4f}")
    print(f"  cos² θ = {cos2_theta:.4f}")
    print(f"  Ω² = ({Omega:.4e})² = {Omega ** 2:.4e} s⁻²")
    print(f"  centrifugal = Ω² r(θ) cos² θ")
    print(f"  centrifugal = ({Omega ** 2:.4e}) × ({r_theta:.0f}) × ({cos2_theta:.4f})")
    print(f"  centrifugal = {centrifugal:.4f} m/s²")

    # Step 5: Calculate theoretical gravity
    g_theoretical = g_grav - centrifugal
    print(f"\nStep 5: Calculate theoretical gravity")
    print(f"  g_theoretical = g_grav - centrifugal")
    print(f"  g_theoretical = {g_grav:.4f} - {centrifugal:.4f}")
    print(f"  g_theoretical = {g_theoretical:.4f} m/s²")

    # =========================================================
    # Part IV(c): Compare with International Gravity Formula
    # =========================================================

    print("\n" + "-" * 60)
    print("Part IV(c) - Comparison with International Gravity Formula")
    print("-" * 60)

    # 1967 International Gravity Formula
    sin2_2theta = np.sin(2 * theta_rad) ** 2
    g_IGF = 9.780318 * (1 + 0.0053024 * sin2_theta - 0.0000058 * sin2_2theta)

    print(f"\nStep 1: Apply International Gravity Formula (1967)")
    print(f"  g(θ) = 9.780318(1 + 0.0053024 sin²θ - 0.0000058 sin²2θ)")
    print(f"  sin² θ = {sin2_theta:.4f}")
    print(f"  sin 2θ = sin({2 * theta_deg:.2f}°) = {np.sin(2 * theta_rad):.4f}")
    print(f"  sin² 2θ = {sin2_2theta:.4f}")
    print(f"  g_IGF = 9.780318(1 + 0.0053024×{sin2_theta:.4f} - 0.0000058×{sin2_2theta:.4f})")
    print(f"  g_IGF = 9.780318(1 + {0.0053024 * sin2_theta:.7f} - {0.0000058 * sin2_2theta:.7f})")
    print(f"  g_IGF = 9.780318(1.0009473) = {g_IGF:.4f} m/s²")

    print(f"\nStep 2: Compare results")
    print(f"  {'Formula':<25} {'Gravity (m/s²)':<15}")
    print(f"  {'-' * 25} {'-' * 15}")
    print(f"  {'Theoretical (from part b)':<25} {g_theoretical:.4f}")
    print(f"  {'IGF 1967':<25} {g_IGF:.4f}")
    print(f"  {'Difference':<25} {g_IGF - g_theoretical:.4f} m/s²")

    print(f"\nStep 3: Explain the difference")
    print(f"""
    The IGF gives a slightly higher value (by about {g_IGF - g_theoretical:.4f} m/s² or
    {(g_IGF - g_theoretical) * 1000:.1f} mGal). The differences arise from:

    1. Earth model assumptions:
       - Theoretical formula assumed a point mass Earth (GM/r²)
       - IGF accounts for actual mass distribution (J₂ term, ellipticity)

    2. Centrifugal treatment:
       - Theoretical formula used simple Ω²r cos²θ
       - IGF incorporates centrifugal effect empirically through latitude dependence

    3. Reference ellipsoid:
       - Theoretical formula used ellipsoid radius but point mass gravitation
       - IGF is based on actual gravity measured on the reference ellipsoid

    4. Higher-order terms:
       - IGF includes sin²2θ term for higher-order moments
       - Simple formula lacks these refinements

    The IGF is empirically derived from actual gravity measurements and is
    more accurate for predicting gravity at any latitude on the reference ellipsoid.
    """)

    iv_results = {
        'g_theoretical': g_theoretical,
        'g_IGF': g_IGF,
        'difference': g_IGF - g_theoretical
    }

    return iv_results


def main():
    """Run all parts of the midterm exam solutions."""

    print("=" * 80)
    print("GOPH 547 - MIDTERM EXAM COMPLETE SOLUTIONS")
    print("=" * 80)

    # Part I
    part_i_answers()

    # Part II
    ii_results = part_ii_solution()

    # Part III
    iii_results = part_iii_solution()

    # Part IV
    iv_results = part_iv_solution()



    print("\nPart II Results:")
    print(f"  g_x = {ii_results['g_x']:.4f} m/s²")
    print(f"  g_y = {ii_results['g_y']:.4f} m/s²")
    print(f"  g_z = {ii_results['g_z']:.4f} m/s²")
    print(f"  ||g|| = {ii_results['g_mag']:.4f} m/s²")
    print(f"  g_r = {ii_results['g_r']:.4f} m/s²")
    print(f"  Total flux through sphere = {ii_results['total_flux']:.3e} m³/s²")
    print(
        f"  θ̂ = ({ii_results['theta_hat'][0]:.4f}, {ii_results['theta_hat'][1]:.4f}, {ii_results['theta_hat'][2]:.4f})")

    print("\nPart III Results:")
    print(f"  Total enclosed mass = {iii_results['M_enc']:.3e} kg")
    print(f"  Flux through hemisphere = {iii_results['flux']:.3e} m³/s²")
    print(f"  Equivalent surface density = {iii_results['rho_star']:.2f} kg/m²")

    print("\nPart IV Results:")
    print(f"  Theoretical gravity at 25.05°N = {iv_results['g_theoretical']:.4f} m/s²")
    print(f"  IGF 1967 gravity at 25.05°N = {iv_results['g_IGF']:.4f} m/s²")
    print(f"  Difference = {iv_results['difference']:.4f} m/s² ({iv_results['difference'] * 1000:.1f} mGal)")


if __name__ == "__main__":
    main()