
Example of inverse CDF
======================

.. code:: python

    # load plotting routines
    
    from bokeh.io import output_notebook, show
    from bokeh.plotting import figure
    from bokeh.layouts import gridplot
    
    output_notebook()



.. raw:: html

    
        <div class="bk-root">
            <a href="http://bokeh.pydata.org" target="_blank" class="bk-logo bk-logo-small bk-logo-notebook"></a>
            <span id="4abeb723-e380-453e-b380-c6f98263a221">Loading BokehJS ...</span>
        </div>




To show the use of the ``inverse_cdf`` library, here we define an
example distribution with two peaks for visual effects.

.. code:: python

    import numpy as np
    from inverse_cdf import inverse_cdf
    
    
    def normal(mu, sigma):
        """Normal distribution."""
        v = sigma**2
        A = (2 * np.pi * v)**(-0.5)
        return lambda x: A * np.exp(-(mu - x)**2 / (2 * v))
    
    
    def pdf(x):
        """Example PDF with two peaks."""
        return (normal(-1.5, 1.0)(x) + normal(2.0, 0.5)(x)) / 2.

.. code:: python

    x = np.linspace(-5, 5, 200)
    fig = figure(plot_width=600, plot_height=400, title='PDF')
    fig.line(x, pdf(x), line_width=2)
    show(fig)


.. image:: pdf.png?raw=true

Now we integrate and plot the inverse cumulative distribution.

.. code:: python

    p = np.linspace(0.0, 1.0, 1025)
    F = inverse_cdf(pdf, -5, 5, 1024)
    
    fig = figure(plot_width=600, plot_height=400, title='iCDF')
    fig.line(p, F, line_width=2)
    show(fig)


.. image:: icdf.png?raw=true

We can use the result to draw a sample following this particular
distribution.

.. code:: python

    icdf = lambda x: np.interp(x, p, F)
    sample = icdf(np.random.uniform(0.0, 1.0, 100000))
    hist, edges = np.histogram(sample, density=True, bins=50)
    
    fig = figure(plot_width=600, plot_height=400, title='sample')
    fig.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
            fill_color="#036564", line_color="#033649")
    fig.line(x, pdf(x), line_width=2, color="#ee8822")
    
    show(fig)


.. image:: sample.png?raw=true

This method can be quite precise, though at the tails of the
distribution the error gets bigger.

.. code:: python

    dp = (p[1:] - p[:-1]) / (F[1:] - F[:-1])
    x = (F[1:] + F[:-1]) / 2.
    
    fig1 = figure(plot_width=600, plot_height=200, title='check PDF')
    fig1.line(x, pdf(x), line_width=4)
    fig1.line(x, dp, line_width=1.5, color='white')
    
    fig2 = figure(plot_width=600, plot_height=400, title='error', y_axis_type="log")
    fig2.line(x, abs(pdf(x) - dp), line_width=1, color='firebrick')
    
    show(gridplot([[fig1],[fig2]]))

.. image:: check.png?raw=true
.. image:: error.png?raw=true

