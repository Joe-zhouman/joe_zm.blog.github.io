# k-epsilon

## standard k-epsilon



The baseline two-transport-equation model solving for kinetic energy k and turbulent dissipation ε. Turbulent dissipation is the rate at which velocity fluctuations dissipate. This is the default k–ε model. Coefficients are empirically derived; valid for fully turbulent flows only. In the standard k-e model, the eddy viscosity is determined from a single turbulence length scale, so the calculated turbulent diffusion is that which occurs only at the specified scale, whereas in reality all scales of motion will contribute to the turbulent diffusion. The k-e model uses the gradient diffusion hypothesis to relate the Reynolds stresses to the mean velocity gradients and the turbulent viscosity. Performs poorly for complex flows involving severe pressure gradient, separation, strong streamline curvature. The most disturbing weakness is lack of sensitivity to adverse pressure gradients; another shortcoming is numerical stiffness when equations are integrated through the viscous sublayer which are treated with damping functions that have stability issues 

F. R. Menter, “Zonal Two Equation k-w Turbulence Models for Aerodynamic Flows,” AIAA Paper #93-2906, 24th Fluid Dynamics Conference, July 1993; 

F. R. Menter, “Two-Equation Eddy-Viscosity Turbulence Models for Engineering Applications,” AIAA Journal, vol. 32, no. 8, pp. 1598-1605, 1994]. 

{Notes: The author’s self-investigation for **flow** through a pipe is consistent with the statements that this model is valid for flows without separation and for fully turbulent **flow**. Compared to a finned problem which had separation and which predicted erroneous results with the k-e model, this pipe **flow** did not have separation and results of k-e and k-w models showed good agreement for high Reynolds numbers. In this pipe **flow**, as Reynolds number was decreased, the difference between the inlet pressures predicted by the k-e and k-w models increased. Note that, based on the author’s limited experience, results for temperature are less sensitive to model choice and for velocity seem indifferent. Pressure results seem highly sensitive to both the model choice and the mesh. Be careful to check all results before deciding that results are valid. For additional details, see section entitled “Comparison of k-e and k-w Models.”}

**Pros**: Robust. Widely used despite the known limitations of the model. Easy to implement. Computationally cheap. Valid for fully turbulent flows only. Suitable for initial iterations, initial screening of alternative designs, and parametric studies.

**Cons**: Performs poorly for complex flows involving severe pressure gradient, separation, strong streamline curvature. Most disturbing weakness is lack of sensitivity to adverse pressure gradients; another shortcoming is numerical stiffness when equations are integrated through the viscous sublayer which are treated with damping functions that have stability issues 

[F. R. Menter, “Zonal Two Equation k-w Turbulence Models for Aerodynamic Flows,” AIAA Paper #93-2906, 24th Fluid Dynamics Conference, July 1993; 

F. R. Menter, “Two-Equation Eddy-Viscosity Turbulence Models for Engineering Applications,” AIAA Journal, vol. 32, no. 8, pp. 1598-1605, 1994].

# k-Omega

## standard k-omega 

A two-transport-equation model solving for kinetic energy k and turbulent frequency ω. This is the default k–ω model. This model allows for a more accurate near wall treatment with an automatic switch from a wall function to a low-Reynolds number formulation based on grid spacing. Demonstrates superior performance for wall-bounded and low Reynolds number flows. Shows potential for predicting transition. Options account for **transitional**, free shear, and compressible flows. The k-e model uses the gradient diffusion hypothesis to relate the Reynolds stresses to the mean velocity gradients and the turbulent viscosity. Solves one equation for turbulent kinetic energy k and a second equation for the specific turbulent dissipation rate (or turbulent frequency) w. This model performs significantly better under adverse pressure gradient conditions. The model does not employ damping functions and has straightforward Dirichlet boundary conditions, which leads to significant advantages in numerical stability. This model underpredicts the amount of separation for severe adverse pressure gradient flows.
Pros: Superior performance for wall-bounded boundary layer, free shear, and low Reynolds number flows. Suitable for complex boundary layer flows under adverse pressure gradient and separation (external aerodynamics and turbomachinery). Can be used for **transitional** flows (though tends to predict early transition).
Cons: Separation is typically predicted to be excessive and early. Requires mesh resolution near the wall.

## BSL k-omega

A variant of the standard k–ω model. Combines the original Wilcox k-w model for use near walls and the standard k–ε model away from walls using a blending function. This eliminates the standard k-w model’s strong sensitivity to free stream conditions without sacrificing near-wall performance.

## SST k-omega

Shear Stress Transport (SST) is a variant of the standard k–ω model. Combines the original Wilcox k-w model for use near walls and the standard k–ε model away from walls using a blending function, and the eddy viscosity formulation is modified to account for the transport effects of the principle turbulent shear stress [F. R. Menter, “Zonal Two Equation k-w Turbulence Models for Aerodynamic Flows,” AIAA Paper #93-2906, 24th Fluid Dynamics Conference, July 1993; F. R. Menter, “Two-Equation Eddy-Viscosity Turbulence Models for Engineering Applications,” AIAA Journal, vol. 32, no. 8, pp. 1598-1605, 1994]. Also limits turbulent viscosity to guarantee that τT~k. The transition and shearing options are borrowed from standard k–ω. No option to include compressibility.

Pros: Offers similar benefits as standard k–ω. The SST model accounts for the transport of turbulent shear stress and gives highly accurate predictions of the onset and the amount of **flow** separation under adverse pressure gradients. SST is recommended for high accuracy boundary layer simulations.

Cons: Dependency on wall distance makes this less suitable for free shear flows compared to standard k-w. Requires mesh resolution near the wall.
A Reynolds Stress model may be more appropriate for flows with sudden changes in strain rate or rotating flows while the SST model may be more appropriate for separated flows.

# 1

I will share my experience with using k-omega SST with low Reynolds number correction vs. k-epsilon model. For a very large multiple liquid/gas systems with conjugate heat transfer and huge amount of radiation we tested both types of turbulence models. The system had both very low velocity **flow** domains and one **flow** domain which was very high temperature, high velocity with jets,re-circulating flows etc. The k-epsilon model (both realizable and RNG) had difficulty converging and seemed to also limit the energy equation from converging as well. The k-omega SST method resulted in more robust convergence and lower oscillation in the residuals. However, as all CFD users know convergence does not equate to accuracy. We have not correlated this model to test data so we cannot verify the accuracy. In addition the mesh was so large and complex that it was impossible to create a boundary layer mesh so we could not guarentee that the y-plus values at the wall were close to 1.0.

We are currently modling another case involving combined turbulence and laminar **flow** (maybe 1% of fluid domain turbulent and the rest laminar) with natural convection and species diffusion. We have experienced a lot of convergence issues using the k-epsilon model and we are now trying the k-omega SST model with low Reynolds Number correction. I will let you know how this turns out.

Overall our experience with the k-omega model has been good but more data needs to be gathered.

# 1

I hope I can still help. I also just started learning but as far as I know you need to change:


\- **RASProperties**: "kEpsilon" to "kOmega" (see pages U-99 & U-184 in User Guide)

\- **transportProperties**: if the fluid stays the same, keep it the same. "nu" is the kinematic viscosity of the fluid (see page U-21 in User Guide)

\- **turbulenceProperties**: keep it "RASModel" since you want to stay in Reynolds-averaged stress modelling (see page U-184 in User Guide)

For **estimating** k and Omega take a look at [**THIS**](http://www.cfd-online.com/Wiki/Turbulence_free-stream_boundary_conditions)

# 1

I have heard so many times saying people SST is a better model than epsilon based models. This may be true if you are interested only in the region where the separation occurs especially for negative pressure gradients. If you are interested in the **flow** development after the attachment, lowRe k-eps or realizable k-epsilon model is definitely a better choice.

I have even seen performing realizable k-epsilon with low y+ treatment model performing better than SST in certain transient flows involving strong **flow** separation. To me it seems that is not right to say that SST is better than k-epsilon.