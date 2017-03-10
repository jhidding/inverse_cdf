
Example of inverse CDF
======================

.. code:: ipython3

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

.. code:: ipython3

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

.. code:: ipython3

    x = np.linspace(-5, 5, 200)
    fig = figure(plot_width=600, plot_height=400, title='PDF')
    fig.line(x, pdf(x), line_width=2)
    show(fig)



.. raw:: html

    
    
        <div class="bk-root">
            <div class="bk-plotdiv" id="4b4cdcae-0ac0-4d3b-a7d3-3f69b2d66795"></div>
        </div>
    <script type="text/javascript">
      
      (function(global) {
        function now() {
          return new Date();
        }
      
        var force = false;
      
        if (typeof (window._bokeh_onload_callbacks) === "undefined" || force === true) {
          window._bokeh_onload_callbacks = [];
          window._bokeh_is_loading = undefined;
        }
      
      
        
        if (typeof (window._bokeh_timeout) === "undefined" || force === true) {
          window._bokeh_timeout = Date.now() + 0;
          window._bokeh_failed_load = false;
        }
      
        var NB_LOAD_WARNING = {'data': {'text/html':
           "<div style='background-color: #fdd'>\n"+
           "<p>\n"+
           "BokehJS does not appear to have successfully loaded. If loading BokehJS from CDN, this \n"+
           "may be due to a slow or bad network connection. Possible fixes:\n"+
           "</p>\n"+
           "<ul>\n"+
           "<li>re-rerun `output_notebook()` to attempt to load from CDN again, or</li>\n"+
           "<li>use INLINE resources instead, as so:</li>\n"+
           "</ul>\n"+
           "<code>\n"+
           "from bokeh.resources import INLINE\n"+
           "output_notebook(resources=INLINE)\n"+
           "</code>\n"+
           "</div>"}};
      
        function display_loaded() {
          if (window.Bokeh !== undefined) {
            document.getElementById("4b4cdcae-0ac0-4d3b-a7d3-3f69b2d66795").textContent = "BokehJS successfully loaded.";
          } else if (Date.now() < window._bokeh_timeout) {
            setTimeout(display_loaded, 100)
          }
        }
      
        function run_callbacks() {
          window._bokeh_onload_callbacks.forEach(function(callback) { callback() });
          delete window._bokeh_onload_callbacks
          console.info("Bokeh: all callbacks have finished");
        }
      
        function load_libs(js_urls, callback) {
          window._bokeh_onload_callbacks.push(callback);
          if (window._bokeh_is_loading > 0) {
            console.log("Bokeh: BokehJS is being loaded, scheduling callback at", now());
            return null;
          }
          if (js_urls == null || js_urls.length === 0) {
            run_callbacks();
            return null;
          }
          console.log("Bokeh: BokehJS not loaded, scheduling load and callback at", now());
          window._bokeh_is_loading = js_urls.length;
          for (var i = 0; i < js_urls.length; i++) {
            var url = js_urls[i];
            var s = document.createElement('script');
            s.src = url;
            s.async = false;
            s.onreadystatechange = s.onload = function() {
              window._bokeh_is_loading--;
              if (window._bokeh_is_loading === 0) {
                console.log("Bokeh: all BokehJS libraries loaded");
                run_callbacks()
              }
            };
            s.onerror = function() {
              console.warn("failed to load library " + url);
            };
            console.log("Bokeh: injecting script tag for BokehJS library: ", url);
            document.getElementsByTagName("head")[0].appendChild(s);
          }
        };var element = document.getElementById("4b4cdcae-0ac0-4d3b-a7d3-3f69b2d66795");
        if (element == null) {
          console.log("Bokeh: ERROR: autoload.js configured with elementid '4b4cdcae-0ac0-4d3b-a7d3-3f69b2d66795' but no matching script tag was found. ")
          return false;
        }
      
        var js_urls = [];
      
        var inline_js = [
          function(Bokeh) {
            (function() {
              var fn = function() {
                var docs_json = {"6e1bd386-c1a8-44e7-bdc2-c972bdefeb4b":{"roots":{"references":[{"attributes":{"active_drag":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"8cae86b6-8e26-467f-9eb3-0f4bb27159f9","type":"PanTool"},{"id":"2566dcd9-be13-4391-b511-b89805a40355","type":"WheelZoomTool"},{"id":"1bc96f0b-8576-4374-9e1f-c73c6aa239ce","type":"BoxZoomTool"},{"id":"4b1d12d3-89ba-4e71-a006-e9c08912fc91","type":"SaveTool"},{"id":"f6148d19-b48f-4351-9c93-0ffb692f9c6f","type":"ResetTool"},{"id":"15dd2129-2c5c-4252-b3d3-06a433061c73","type":"HelpTool"}]},"id":"46d76ccc-7634-49f6-9d10-1c815554fdb6","type":"Toolbar"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"00554e85-07aa-434d-9168-6c473c62344c","type":"BoxAnnotation"},{"attributes":{"plot":null,"text":"PDF"},"id":"6111b897-862c-4d53-8e6b-f95cfc37f52a","type":"Title"},{"attributes":{"callback":null,"column_names":["y","x"],"data":{"x":{"__ndarray__":"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","dtype":"float64","shape":[200]},"y":{"__ndarray__":"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","dtype":"float64","shape":[200]}}},"id":"b75c86d0-3e55-4bf9-98e0-cf965ab6d7e8","type":"ColumnDataSource"},{"attributes":{"dimension":1,"plot":{"id":"9b67ee62-13e7-4050-81b5-18d59f90f978","subtype":"Figure","type":"Plot"},"ticker":{"id":"f252d1e6-19f1-47cd-8efd-909e76715023","type":"BasicTicker"}},"id":"7c54a4a7-2a11-4d78-9df6-ed95296ef779","type":"Grid"},{"attributes":{"plot":{"id":"9b67ee62-13e7-4050-81b5-18d59f90f978","subtype":"Figure","type":"Plot"}},"id":"8cae86b6-8e26-467f-9eb3-0f4bb27159f9","type":"PanTool"},{"attributes":{"plot":{"id":"9b67ee62-13e7-4050-81b5-18d59f90f978","subtype":"Figure","type":"Plot"}},"id":"2566dcd9-be13-4391-b511-b89805a40355","type":"WheelZoomTool"},{"attributes":{"formatter":{"id":"e42922ff-718e-47f7-afbc-7548eb469aa1","type":"BasicTickFormatter"},"plot":{"id":"9b67ee62-13e7-4050-81b5-18d59f90f978","subtype":"Figure","type":"Plot"},"ticker":{"id":"a1f9e1bc-0877-43f9-9d57-49e252a500c4","type":"BasicTicker"}},"id":"42a0d1ad-5528-4c67-828b-030ac3475c1c","type":"LinearAxis"},{"attributes":{"plot":{"id":"9b67ee62-13e7-4050-81b5-18d59f90f978","subtype":"Figure","type":"Plot"},"ticker":{"id":"a1f9e1bc-0877-43f9-9d57-49e252a500c4","type":"BasicTicker"}},"id":"df87f643-c9ee-4d36-a0bc-e55bc574daba","type":"Grid"},{"attributes":{},"id":"a1f9e1bc-0877-43f9-9d57-49e252a500c4","type":"BasicTicker"},{"attributes":{"callback":null},"id":"1aca969c-4cde-4b79-b134-f4e54b29bf8b","type":"DataRange1d"},{"attributes":{"formatter":{"id":"0463c1e8-bad4-45c9-b1c1-bd1c59b35989","type":"BasicTickFormatter"},"plot":{"id":"9b67ee62-13e7-4050-81b5-18d59f90f978","subtype":"Figure","type":"Plot"},"ticker":{"id":"f252d1e6-19f1-47cd-8efd-909e76715023","type":"BasicTicker"}},"id":"11676def-ba41-41b0-8a9d-4f2bb3a7c9a4","type":"LinearAxis"},{"attributes":{"overlay":{"id":"00554e85-07aa-434d-9168-6c473c62344c","type":"BoxAnnotation"},"plot":{"id":"9b67ee62-13e7-4050-81b5-18d59f90f978","subtype":"Figure","type":"Plot"}},"id":"1bc96f0b-8576-4374-9e1f-c73c6aa239ce","type":"BoxZoomTool"},{"attributes":{"plot":{"id":"9b67ee62-13e7-4050-81b5-18d59f90f978","subtype":"Figure","type":"Plot"}},"id":"4b1d12d3-89ba-4e71-a006-e9c08912fc91","type":"SaveTool"},{"attributes":{"below":[{"id":"42a0d1ad-5528-4c67-828b-030ac3475c1c","type":"LinearAxis"}],"left":[{"id":"11676def-ba41-41b0-8a9d-4f2bb3a7c9a4","type":"LinearAxis"}],"plot_height":400,"renderers":[{"id":"42a0d1ad-5528-4c67-828b-030ac3475c1c","type":"LinearAxis"},{"id":"df87f643-c9ee-4d36-a0bc-e55bc574daba","type":"Grid"},{"id":"11676def-ba41-41b0-8a9d-4f2bb3a7c9a4","type":"LinearAxis"},{"id":"7c54a4a7-2a11-4d78-9df6-ed95296ef779","type":"Grid"},{"id":"00554e85-07aa-434d-9168-6c473c62344c","type":"BoxAnnotation"},{"id":"3154e497-769c-4021-bf24-948aa73e1887","type":"GlyphRenderer"}],"title":{"id":"6111b897-862c-4d53-8e6b-f95cfc37f52a","type":"Title"},"tool_events":{"id":"2d5442d7-aa4a-4d65-9758-73e01af397e6","type":"ToolEvents"},"toolbar":{"id":"46d76ccc-7634-49f6-9d10-1c815554fdb6","type":"Toolbar"},"x_range":{"id":"1aca969c-4cde-4b79-b134-f4e54b29bf8b","type":"DataRange1d"},"y_range":{"id":"2ca74f83-c98b-4eda-804c-9ff2da6dd836","type":"DataRange1d"}},"id":"9b67ee62-13e7-4050-81b5-18d59f90f978","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"f252d1e6-19f1-47cd-8efd-909e76715023","type":"BasicTicker"},{"attributes":{"plot":{"id":"9b67ee62-13e7-4050-81b5-18d59f90f978","subtype":"Figure","type":"Plot"}},"id":"f6148d19-b48f-4351-9c93-0ffb692f9c6f","type":"ResetTool"},{"attributes":{"plot":{"id":"9b67ee62-13e7-4050-81b5-18d59f90f978","subtype":"Figure","type":"Plot"}},"id":"15dd2129-2c5c-4252-b3d3-06a433061c73","type":"HelpTool"},{"attributes":{"data_source":{"id":"b75c86d0-3e55-4bf9-98e0-cf965ab6d7e8","type":"ColumnDataSource"},"glyph":{"id":"ef291c8d-2877-40e6-b432-01247bc707e6","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"449062f4-84c0-410b-8cf9-5638f8207e60","type":"Line"},"selection_glyph":null},"id":"3154e497-769c-4021-bf24-948aa73e1887","type":"GlyphRenderer"},{"attributes":{},"id":"0463c1e8-bad4-45c9-b1c1-bd1c59b35989","type":"BasicTickFormatter"},{"attributes":{},"id":"2d5442d7-aa4a-4d65-9758-73e01af397e6","type":"ToolEvents"},{"attributes":{"line_color":{"value":"#1f77b4"},"line_width":{"value":2},"x":{"field":"x"},"y":{"field":"y"}},"id":"ef291c8d-2877-40e6-b432-01247bc707e6","type":"Line"},{"attributes":{},"id":"e42922ff-718e-47f7-afbc-7548eb469aa1","type":"BasicTickFormatter"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"line_width":{"value":2},"x":{"field":"x"},"y":{"field":"y"}},"id":"449062f4-84c0-410b-8cf9-5638f8207e60","type":"Line"},{"attributes":{"callback":null},"id":"2ca74f83-c98b-4eda-804c-9ff2da6dd836","type":"DataRange1d"}],"root_ids":["9b67ee62-13e7-4050-81b5-18d59f90f978"]},"title":"Bokeh Application","version":"0.12.4"}};
                var render_items = [{"docid":"6e1bd386-c1a8-44e7-bdc2-c972bdefeb4b","elementid":"4b4cdcae-0ac0-4d3b-a7d3-3f69b2d66795","modelid":"9b67ee62-13e7-4050-81b5-18d59f90f978"}];
                
                Bokeh.embed.embed_items(docs_json, render_items);
              };
              if (document.readyState != "loading") fn();
              else document.addEventListener("DOMContentLoaded", fn);
            })();
          },
          function(Bokeh) {
          }
        ];
      
        function run_inline_js() {
          
          if ((window.Bokeh !== undefined) || (force === true)) {
            for (var i = 0; i < inline_js.length; i++) {
              inline_js[i](window.Bokeh);
            }if (force === true) {
              display_loaded();
            }} else if (Date.now() < window._bokeh_timeout) {
            setTimeout(run_inline_js, 100);
          } else if (!window._bokeh_failed_load) {
            console.log("Bokeh: BokehJS failed to load within specified timeout.");
            window._bokeh_failed_load = true;
          } else if (force !== true) {
            var cell = $(document.getElementById("4b4cdcae-0ac0-4d3b-a7d3-3f69b2d66795")).parents('.cell').data().cell;
            cell.output_area.append_execute_result(NB_LOAD_WARNING)
          }
      
        }
      
        if (window._bokeh_is_loading === 0) {
          console.log("Bokeh: BokehJS loaded, going straight to plotting");
          run_inline_js();
        } else {
          load_libs(js_urls, function() {
            console.log("Bokeh: BokehJS plotting callback run at", now());
            run_inline_js();
          });
        }
      }(this));
    </script>


Now we integrate and plot the inverse cumulative distribution.

.. code:: ipython3

    p = np.linspace(0.0, 1.0, 1025)
    F = inverse_cdf(pdf, -5, 5, 1024)
    
    fig = figure(plot_width=600, plot_height=400, title='iCDF')
    fig.line(p, F, line_width=2)
    show(fig)



.. raw:: html

    
    
        <div class="bk-root">
            <div class="bk-plotdiv" id="c3a41ab7-b98d-40a2-ad42-55a08cd244c3"></div>
        </div>
    <script type="text/javascript">
      
      (function(global) {
        function now() {
          return new Date();
        }
      
        var force = false;
      
        if (typeof (window._bokeh_onload_callbacks) === "undefined" || force === true) {
          window._bokeh_onload_callbacks = [];
          window._bokeh_is_loading = undefined;
        }
      
      
        
        if (typeof (window._bokeh_timeout) === "undefined" || force === true) {
          window._bokeh_timeout = Date.now() + 0;
          window._bokeh_failed_load = false;
        }
      
        var NB_LOAD_WARNING = {'data': {'text/html':
           "<div style='background-color: #fdd'>\n"+
           "<p>\n"+
           "BokehJS does not appear to have successfully loaded. If loading BokehJS from CDN, this \n"+
           "may be due to a slow or bad network connection. Possible fixes:\n"+
           "</p>\n"+
           "<ul>\n"+
           "<li>re-rerun `output_notebook()` to attempt to load from CDN again, or</li>\n"+
           "<li>use INLINE resources instead, as so:</li>\n"+
           "</ul>\n"+
           "<code>\n"+
           "from bokeh.resources import INLINE\n"+
           "output_notebook(resources=INLINE)\n"+
           "</code>\n"+
           "</div>"}};
      
        function display_loaded() {
          if (window.Bokeh !== undefined) {
            document.getElementById("c3a41ab7-b98d-40a2-ad42-55a08cd244c3").textContent = "BokehJS successfully loaded.";
          } else if (Date.now() < window._bokeh_timeout) {
            setTimeout(display_loaded, 100)
          }
        }
      
        function run_callbacks() {
          window._bokeh_onload_callbacks.forEach(function(callback) { callback() });
          delete window._bokeh_onload_callbacks
          console.info("Bokeh: all callbacks have finished");
        }
      
        function load_libs(js_urls, callback) {
          window._bokeh_onload_callbacks.push(callback);
          if (window._bokeh_is_loading > 0) {
            console.log("Bokeh: BokehJS is being loaded, scheduling callback at", now());
            return null;
          }
          if (js_urls == null || js_urls.length === 0) {
            run_callbacks();
            return null;
          }
          console.log("Bokeh: BokehJS not loaded, scheduling load and callback at", now());
          window._bokeh_is_loading = js_urls.length;
          for (var i = 0; i < js_urls.length; i++) {
            var url = js_urls[i];
            var s = document.createElement('script');
            s.src = url;
            s.async = false;
            s.onreadystatechange = s.onload = function() {
              window._bokeh_is_loading--;
              if (window._bokeh_is_loading === 0) {
                console.log("Bokeh: all BokehJS libraries loaded");
                run_callbacks()
              }
            };
            s.onerror = function() {
              console.warn("failed to load library " + url);
            };
            console.log("Bokeh: injecting script tag for BokehJS library: ", url);
            document.getElementsByTagName("head")[0].appendChild(s);
          }
        };var element = document.getElementById("c3a41ab7-b98d-40a2-ad42-55a08cd244c3");
        if (element == null) {
          console.log("Bokeh: ERROR: autoload.js configured with elementid 'c3a41ab7-b98d-40a2-ad42-55a08cd244c3' but no matching script tag was found. ")
          return false;
        }
      
        var js_urls = [];
      
        var inline_js = [
          function(Bokeh) {
            (function() {
              var fn = function() {
                var docs_json = {"41216d9a-518f-44b7-baa4-b709f5bcfc01":{"roots":{"references":[{"attributes":{"plot":{"id":"9276a086-04e5-4aa1-ba5b-95700a9cfe1d","subtype":"Figure","type":"Plot"},"ticker":{"id":"4e5da7ac-f3b0-4544-9d32-d00868060ef9","type":"BasicTicker"}},"id":"baa71abd-3203-4511-b407-51698e05ffac","type":"Grid"},{"attributes":{"below":[{"id":"698835c5-0ea2-4ad7-8d19-4e5772cff378","type":"LinearAxis"}],"left":[{"id":"981b2b35-1079-435d-8ed1-f59af2643234","type":"LinearAxis"}],"plot_height":400,"renderers":[{"id":"698835c5-0ea2-4ad7-8d19-4e5772cff378","type":"LinearAxis"},{"id":"baa71abd-3203-4511-b407-51698e05ffac","type":"Grid"},{"id":"981b2b35-1079-435d-8ed1-f59af2643234","type":"LinearAxis"},{"id":"86d233c6-26c0-40e9-8a2b-e08ec9dc5d28","type":"Grid"},{"id":"6ef4fcab-4d59-4682-b711-c1f607fb7493","type":"BoxAnnotation"},{"id":"1b211779-22e3-4b4b-8e82-5342aa787ee5","type":"GlyphRenderer"}],"title":{"id":"69288a46-6504-4a7a-8815-46455133f8e0","type":"Title"},"tool_events":{"id":"d0c5d278-c599-4070-a42b-4b0ceea8226b","type":"ToolEvents"},"toolbar":{"id":"cdd8361b-ae88-4644-9c23-18a12558ff96","type":"Toolbar"},"x_range":{"id":"cad311bf-b18e-4450-9df0-a4a98a35db53","type":"DataRange1d"},"y_range":{"id":"d26066fb-46d5-4a43-86fb-37c2426c3dd3","type":"DataRange1d"}},"id":"9276a086-04e5-4aa1-ba5b-95700a9cfe1d","subtype":"Figure","type":"Plot"},{"attributes":{"plot":{"id":"9276a086-04e5-4aa1-ba5b-95700a9cfe1d","subtype":"Figure","type":"Plot"}},"id":"469c2472-5634-4d65-985a-5d449ba05699","type":"PanTool"},{"attributes":{},"id":"40035d38-0d15-4ce4-9112-b5bed0728917","type":"BasicTickFormatter"},{"attributes":{},"id":"735c78a1-bb71-4b90-ae6b-781ac1d76ec1","type":"BasicTicker"},{"attributes":{"active_drag":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"469c2472-5634-4d65-985a-5d449ba05699","type":"PanTool"},{"id":"d4d8eabb-8511-41a9-9f01-e030c4d0d90b","type":"WheelZoomTool"},{"id":"2d9f2274-d6c3-4076-b712-094091b254f4","type":"BoxZoomTool"},{"id":"53071495-b204-45f2-9d79-ee16be23f7ef","type":"SaveTool"},{"id":"5a65995a-85db-4296-8494-b00a14bf7252","type":"ResetTool"},{"id":"a9c1974f-40d8-42a0-bfaf-8bc7566d624b","type":"HelpTool"}]},"id":"cdd8361b-ae88-4644-9c23-18a12558ff96","type":"Toolbar"},{"attributes":{"plot":null,"text":"iCDF"},"id":"69288a46-6504-4a7a-8815-46455133f8e0","type":"Title"},{"attributes":{"plot":{"id":"9276a086-04e5-4aa1-ba5b-95700a9cfe1d","subtype":"Figure","type":"Plot"}},"id":"d4d8eabb-8511-41a9-9f01-e030c4d0d90b","type":"WheelZoomTool"},{"attributes":{"formatter":{"id":"99e81bc7-10a0-4e60-a088-93f94613d06f","type":"BasicTickFormatter"},"plot":{"id":"9276a086-04e5-4aa1-ba5b-95700a9cfe1d","subtype":"Figure","type":"Plot"},"ticker":{"id":"4e5da7ac-f3b0-4544-9d32-d00868060ef9","type":"BasicTicker"}},"id":"698835c5-0ea2-4ad7-8d19-4e5772cff378","type":"LinearAxis"},{"attributes":{"dimension":1,"plot":{"id":"9276a086-04e5-4aa1-ba5b-95700a9cfe1d","subtype":"Figure","type":"Plot"},"ticker":{"id":"735c78a1-bb71-4b90-ae6b-781ac1d76ec1","type":"BasicTicker"}},"id":"86d233c6-26c0-40e9-8a2b-e08ec9dc5d28","type":"Grid"},{"attributes":{},"id":"d0c5d278-c599-4070-a42b-4b0ceea8226b","type":"ToolEvents"},{"attributes":{},"id":"99e81bc7-10a0-4e60-a088-93f94613d06f","type":"BasicTickFormatter"},{"attributes":{},"id":"4e5da7ac-f3b0-4544-9d32-d00868060ef9","type":"BasicTicker"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"6ef4fcab-4d59-4682-b711-c1f607fb7493","type":"BoxAnnotation"},{"attributes":{"callback":null},"id":"d26066fb-46d5-4a43-86fb-37c2426c3dd3","type":"DataRange1d"},{"attributes":{"overlay":{"id":"6ef4fcab-4d59-4682-b711-c1f607fb7493","type":"BoxAnnotation"},"plot":{"id":"9276a086-04e5-4aa1-ba5b-95700a9cfe1d","subtype":"Figure","type":"Plot"}},"id":"2d9f2274-d6c3-4076-b712-094091b254f4","type":"BoxZoomTool"},{"attributes":{"plot":{"id":"9276a086-04e5-4aa1-ba5b-95700a9cfe1d","subtype":"Figure","type":"Plot"}},"id":"a9c1974f-40d8-42a0-bfaf-8bc7566d624b","type":"HelpTool"},{"attributes":{"data_source":{"id":"1e08a4da-ac3e-4769-9065-0f582b89d6b6","type":"ColumnDataSource"},"glyph":{"id":"1f7163a8-8d66-40c3-bc3a-d2c1919d2132","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"56d9845b-4767-4a71-b7cf-9c658823ad7b","type":"Line"},"selection_glyph":null},"id":"1b211779-22e3-4b4b-8e82-5342aa787ee5","type":"GlyphRenderer"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"line_width":{"value":2},"x":{"field":"x"},"y":{"field":"y"}},"id":"56d9845b-4767-4a71-b7cf-9c658823ad7b","type":"Line"},{"attributes":{"plot":{"id":"9276a086-04e5-4aa1-ba5b-95700a9cfe1d","subtype":"Figure","type":"Plot"}},"id":"5a65995a-85db-4296-8494-b00a14bf7252","type":"ResetTool"},{"attributes":{"plot":{"id":"9276a086-04e5-4aa1-ba5b-95700a9cfe1d","subtype":"Figure","type":"Plot"}},"id":"53071495-b204-45f2-9d79-ee16be23f7ef","type":"SaveTool"},{"attributes":{"callback":null,"column_names":["y","x"],"data":{"x":{"__ndarray__":"AAAAAAAAAAAAAAAAAABQPwAAAAAAAGA/AAAAAAAAaD8AAAAAAABwPwAAAAAAAHQ/AAAAAAAAeD8AAAAAAAB8PwAAAAAAAIA/AAAAAAAAgj8AAAAAAACEPwAAAAAAAIY/AAAAAAAAiD8AAAAAAACKPwAAAAAAAIw/AAAAAAAAjj8AAAAAAACQPwAAAAAAAJE/AAAAAAAAkj8AAAAAAACTPwAAAAAAAJQ/AAAAAAAAlT8AAAAAAACWPwAAAAAAAJc/AAAAAAAAmD8AAAAAAACZPwAAAAAAAJo/AAAAAAAAmz8AAAAAAACcPwAAAAAAAJ0/AAAAAAAAnj8AAAAAAACfPwAAAAAAAKA/AAAAAACAoD8AAAAAAAChPwAAAAAAgKE/AAAAAAAAoj8AAAAAAICiPwAAAAAAAKM/AAAAAACAoz8AAAAAAACkPwAAAAAAgKQ/AAAAAAAApT8AAAAAAIClPwAAAAAAAKY/AAAAAACApj8AAAAAAACnPwAAAAAAgKc/AAAAAAAAqD8AAAAAAICoPwAAAAAAAKk/AAAAAACAqT8AAAAAAACqPwAAAAAAgKo/AAAAAAAAqz8AAAAAAICrPwAAAAAAAKw/AAAAAACArD8AAAAAAACtPwAAAAAAgK0/AAAAAAAArj8AAAAAAICuPwAAAAAAAK8/AAAAAACArz8AAAAAAACwPwAAAAAAQLA/AAAAAACAsD8AAAAAAMCwPwAAAAAAALE/AAAAAABAsT8AAAAAAICxPwAAAAAAwLE/AAAAAAAAsj8AAAAAAECyPwAAAAAAgLI/AAAAAADAsj8AAAAAAACzPwAAAAAAQLM/AAAAAACAsz8AAAAAAMCzPwAAAAAAALQ/AAAAAABAtD8AAAAAAIC0PwAAAAAAwLQ/AAAAAAAAtT8AAAAAAEC1PwAAAAAAgLU/AAAAAADAtT8AAAAAAAC2PwAAAAAAQLY/AAAAAACAtj8AAAAAAMC2PwAAAAAAALc/AAAAAABAtz8AAAAAAIC3PwAAAAAAwLc/AAAAAAAAuD8AAAAAAEC4PwAAAAAAgLg/AAAAAADAuD8AAAAAAAC5PwAAAAAAQLk/AAAAAACAuT8AAAAAAMC5PwAAAAAAALo/AAAAAABAuj8AAAAAAIC6PwAAAAAAwLo/AAAAAAAAuz8AAAAAAEC7PwAAAAAAgLs/AAAAAADAuz8AAAAAAAC8PwAAAAAAQLw/AAAAAACAvD8AAAAAAMC8PwAAAAAAAL0/AAAAAABAvT8AAAAAAIC9PwAAAAAAwL0/AAAAAAAAvj8AAAAAAEC+PwAAAAAAgL4/AAAAAADAvj8AAAAAAAC/PwAAAAAAQL8/AAAAAACAvz8AAAAAAMC/PwAAAAAAAMA/AAAAAAAgwD8AAAAAAEDAPwAAAAAAYMA/AAAAAACAwD8AAAAAAKDAPwAAAAAAwMA/AAAAAADgwD8AAAAAAADBPwAAAAAAIME/AAAAAABAwT8AAAAAAGDBPwAAAAAAgME/AAAAAACgwT8AAAAAAMDBPwAAAAAA4ME/AAAAAAAAwj8AAAAAACDCPwAAAAAAQMI/AAAAAABgwj8AAAAAAIDCPwAAAAAAoMI/AAAAAADAwj8AAAAAAODCPwAAAAAAAMM/AAAAAAAgwz8AAAAAAEDDPwAAAAAAYMM/AAAAAACAwz8AAAAAAKDDPwAAAAAAwMM/AAAAAADgwz8AAAAAAADEPwAAAAAAIMQ/AAAAAABAxD8AAAAAAGDEPwAAAAAAgMQ/AAAAAACgxD8AAAAAAMDEPwAAAAAA4MQ/AAAAAAAAxT8AAAAAACDFPwAAAAAAQMU/AAAAAABgxT8AAAAAAIDFPwAAAAAAoMU/AAAAAADAxT8AAAAAAODFPwAAAAAAAMY/AAAAAAAgxj8AAAAAAEDGPwAAAAAAYMY/AAAAAACAxj8AAAAAAKDGPwAAAAAAwMY/AAAAAADgxj8AAAAAAADHPwAAAAAAIMc/AAAAAABAxz8AAAAAAGDHPwAAAAAAgMc/AAAAAACgxz8AAAAAAMDHPwAAAAAA4Mc/AAAAAAAAyD8AAAAAACDIPwAAAAAAQMg/AAAAAABgyD8AAAAAAIDIPwAAAAAAoMg/AAAAAADAyD8AAAAAAODIPwAAAAAAAMk/AAAAAAAgyT8AAAAAAEDJPwAAAAAAYMk/AAAAAACAyT8AAAAAAKDJPwAAAAAAwMk/AAAAAADgyT8AAAAAAADKPwAAAAAAIMo/AAAAAABAyj8AAAAAAGDKPwAAAAAAgMo/AAAAAACgyj8AAAAAAMDKPwAAAAAA4Mo/AAAAAAAAyz8AAAAAACDLPwAAAAAAQMs/AAAAAABgyz8AAAAAAIDLPwAAAAAAoMs/AAAAAADAyz8AAAAAAODLPwAAAAAAAMw/AAAAAAAgzD8AAAAAAEDMPwAAAAAAYMw/AAAAAACAzD8AAAAAAKDMPwAAAAAAwMw/AAAAAADgzD8AAAAAAADNPwAAAAAAIM0/AAAAAABAzT8AAAAAAGDNPwAAAAAAgM0/AAAAAACgzT8AAAAAAMDNPwAAAAAA4M0/AAAAAAAAzj8AAAAAACDOPwAAAAAAQM4/AAAAAABgzj8AAAAAAIDOPwAAAAAAoM4/AAAAAADAzj8AAAAAAODOPwAAAAAAAM8/AAAAAAAgzz8AAAAAAEDPPwAAAAAAYM8/AAAAAACAzz8AAAAAAKDPPwAAAAAAwM8/AAAAAADgzz8AAAAAAADQPwAAAAAAENA/AAAAAAAg0D8AAAAAADDQPwAAAAAAQNA/AAAAAABQ0D8AAAAAAGDQPwAAAAAAcNA/AAAAAACA0D8AAAAAAJDQPwAAAAAAoNA/AAAAAACw0D8AAAAAAMDQPwAAAAAA0NA/AAAAAADg0D8AAAAAAPDQPwAAAAAAANE/AAAAAAAQ0T8AAAAAACDRPwAAAAAAMNE/AAAAAABA0T8AAAAAAFDRPwAAAAAAYNE/AAAAAABw0T8AAAAAAIDRPwAAAAAAkNE/AAAAAACg0T8AAAAAALDRPwAAAAAAwNE/AAAAAADQ0T8AAAAAAODRPwAAAAAA8NE/AAAAAAAA0j8AAAAAABDSPwAAAAAAINI/AAAAAAAw0j8AAAAAAEDSPwAAAAAAUNI/AAAAAABg0j8AAAAAAHDSPwAAAAAAgNI/AAAAAACQ0j8AAAAAAKDSPwAAAAAAsNI/AAAAAADA0j8AAAAAANDSPwAAAAAA4NI/AAAAAADw0j8AAAAAAADTPwAAAAAAENM/AAAAAAAg0z8AAAAAADDTPwAAAAAAQNM/AAAAAABQ0z8AAAAAAGDTPwAAAAAAcNM/AAAAAACA0z8AAAAAAJDTPwAAAAAAoNM/AAAAAACw0z8AAAAAAMDTPwAAAAAA0NM/AAAAAADg0z8AAAAAAPDTPwAAAAAAANQ/AAAAAAAQ1D8AAAAAACDUPwAAAAAAMNQ/AAAAAABA1D8AAAAAAFDUPwAAAAAAYNQ/AAAAAABw1D8AAAAAAIDUPwAAAAAAkNQ/AAAAAACg1D8AAAAAALDUPwAAAAAAwNQ/AAAAAADQ1D8AAAAAAODUPwAAAAAA8NQ/AAAAAAAA1T8AAAAA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","dtype":"float64","shape":[1025]},"y":{"__ndarray__":"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","dtype":"float32","shape":[1025]}}},"id":"1e08a4da-ac3e-4769-9065-0f582b89d6b6","type":"ColumnDataSource"},{"attributes":{"callback":null},"id":"cad311bf-b18e-4450-9df0-a4a98a35db53","type":"DataRange1d"},{"attributes":{"line_color":{"value":"#1f77b4"},"line_width":{"value":2},"x":{"field":"x"},"y":{"field":"y"}},"id":"1f7163a8-8d66-40c3-bc3a-d2c1919d2132","type":"Line"},{"attributes":{"formatter":{"id":"40035d38-0d15-4ce4-9112-b5bed0728917","type":"BasicTickFormatter"},"plot":{"id":"9276a086-04e5-4aa1-ba5b-95700a9cfe1d","subtype":"Figure","type":"Plot"},"ticker":{"id":"735c78a1-bb71-4b90-ae6b-781ac1d76ec1","type":"BasicTicker"}},"id":"981b2b35-1079-435d-8ed1-f59af2643234","type":"LinearAxis"}],"root_ids":["9276a086-04e5-4aa1-ba5b-95700a9cfe1d"]},"title":"Bokeh Application","version":"0.12.4"}};
                var render_items = [{"docid":"41216d9a-518f-44b7-baa4-b709f5bcfc01","elementid":"c3a41ab7-b98d-40a2-ad42-55a08cd244c3","modelid":"9276a086-04e5-4aa1-ba5b-95700a9cfe1d"}];
                
                Bokeh.embed.embed_items(docs_json, render_items);
              };
              if (document.readyState != "loading") fn();
              else document.addEventListener("DOMContentLoaded", fn);
            })();
          },
          function(Bokeh) {
          }
        ];
      
        function run_inline_js() {
          
          if ((window.Bokeh !== undefined) || (force === true)) {
            for (var i = 0; i < inline_js.length; i++) {
              inline_js[i](window.Bokeh);
            }if (force === true) {
              display_loaded();
            }} else if (Date.now() < window._bokeh_timeout) {
            setTimeout(run_inline_js, 100);
          } else if (!window._bokeh_failed_load) {
            console.log("Bokeh: BokehJS failed to load within specified timeout.");
            window._bokeh_failed_load = true;
          } else if (force !== true) {
            var cell = $(document.getElementById("c3a41ab7-b98d-40a2-ad42-55a08cd244c3")).parents('.cell').data().cell;
            cell.output_area.append_execute_result(NB_LOAD_WARNING)
          }
      
        }
      
        if (window._bokeh_is_loading === 0) {
          console.log("Bokeh: BokehJS loaded, going straight to plotting");
          run_inline_js();
        } else {
          load_libs(js_urls, function() {
            console.log("Bokeh: BokehJS plotting callback run at", now());
            run_inline_js();
          });
        }
      }(this));
    </script>


We can use the result to draw a sample following this particular
distribution.

.. code:: ipython3

    icdf = lambda x: np.interp(x, p, F)
    sample = icdf(np.random.uniform(0.0, 1.0, 100000))
    hist, edges = np.histogram(sample, density=True, bins=50)
    
    fig = figure(plot_width=600, plot_height=400, title='sample')
    fig.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
            fill_color="#036564", line_color="#033649")
    fig.line(x, pdf(x), line_width=2, color="#ee8822")
    
    show(fig)



.. raw:: html

    
    
        <div class="bk-root">
            <div class="bk-plotdiv" id="838fb569-164e-4414-a2f1-f2516169e1b3"></div>
        </div>
    <script type="text/javascript">
      
      (function(global) {
        function now() {
          return new Date();
        }
      
        var force = false;
      
        if (typeof (window._bokeh_onload_callbacks) === "undefined" || force === true) {
          window._bokeh_onload_callbacks = [];
          window._bokeh_is_loading = undefined;
        }
      
      
        
        if (typeof (window._bokeh_timeout) === "undefined" || force === true) {
          window._bokeh_timeout = Date.now() + 0;
          window._bokeh_failed_load = false;
        }
      
        var NB_LOAD_WARNING = {'data': {'text/html':
           "<div style='background-color: #fdd'>\n"+
           "<p>\n"+
           "BokehJS does not appear to have successfully loaded. If loading BokehJS from CDN, this \n"+
           "may be due to a slow or bad network connection. Possible fixes:\n"+
           "</p>\n"+
           "<ul>\n"+
           "<li>re-rerun `output_notebook()` to attempt to load from CDN again, or</li>\n"+
           "<li>use INLINE resources instead, as so:</li>\n"+
           "</ul>\n"+
           "<code>\n"+
           "from bokeh.resources import INLINE\n"+
           "output_notebook(resources=INLINE)\n"+
           "</code>\n"+
           "</div>"}};
      
        function display_loaded() {
          if (window.Bokeh !== undefined) {
            document.getElementById("838fb569-164e-4414-a2f1-f2516169e1b3").textContent = "BokehJS successfully loaded.";
          } else if (Date.now() < window._bokeh_timeout) {
            setTimeout(display_loaded, 100)
          }
        }
      
        function run_callbacks() {
          window._bokeh_onload_callbacks.forEach(function(callback) { callback() });
          delete window._bokeh_onload_callbacks
          console.info("Bokeh: all callbacks have finished");
        }
      
        function load_libs(js_urls, callback) {
          window._bokeh_onload_callbacks.push(callback);
          if (window._bokeh_is_loading > 0) {
            console.log("Bokeh: BokehJS is being loaded, scheduling callback at", now());
            return null;
          }
          if (js_urls == null || js_urls.length === 0) {
            run_callbacks();
            return null;
          }
          console.log("Bokeh: BokehJS not loaded, scheduling load and callback at", now());
          window._bokeh_is_loading = js_urls.length;
          for (var i = 0; i < js_urls.length; i++) {
            var url = js_urls[i];
            var s = document.createElement('script');
            s.src = url;
            s.async = false;
            s.onreadystatechange = s.onload = function() {
              window._bokeh_is_loading--;
              if (window._bokeh_is_loading === 0) {
                console.log("Bokeh: all BokehJS libraries loaded");
                run_callbacks()
              }
            };
            s.onerror = function() {
              console.warn("failed to load library " + url);
            };
            console.log("Bokeh: injecting script tag for BokehJS library: ", url);
            document.getElementsByTagName("head")[0].appendChild(s);
          }
        };var element = document.getElementById("838fb569-164e-4414-a2f1-f2516169e1b3");
        if (element == null) {
          console.log("Bokeh: ERROR: autoload.js configured with elementid '838fb569-164e-4414-a2f1-f2516169e1b3' but no matching script tag was found. ")
          return false;
        }
      
        var js_urls = [];
      
        var inline_js = [
          function(Bokeh) {
            (function() {
              var fn = function() {
                var docs_json = {"0f3b9193-dd48-49ee-b76e-fa3f2694fa39":{"roots":{"references":[{"attributes":{"formatter":{"id":"73d40397-a7a4-4e1e-a93d-b55a98053635","type":"BasicTickFormatter"},"plot":{"id":"5e8774d8-6ca4-43bd-ad11-257bab2ace33","subtype":"Figure","type":"Plot"},"ticker":{"id":"9c5db322-3d2b-4fb8-b3fa-25c854978cb7","type":"BasicTicker"}},"id":"51abae62-c7d6-4d77-9650-fed60c3e54a9","type":"LinearAxis"},{"attributes":{"callback":null,"column_names":["left","top","right"],"data":{"left":{"__ndarray__":"Wr1sZNn8E8Asx49lODATwP/QsmaXYxLA0drVZ/aWEcCj5PhoVcoQwOvcN9Ro+w/AkPB91iZiDsA0BMTY5MgMwNkXCtuiLwvAfitQ3WCWCcAiP5bfHv0HwMdS3OHcYwbAbGYi5JrKBMAQemjmWDEDwLWNrugWmAHAskLp1an9/7/8aXXaJcv8v0aRAd+hmPm/jriN4x1m9r/Y3xnomTPzvyAHpuwVAfC/2Fxk4iOd6b9oq3zrGzjjv/DzKeknptm/QCK19i+4yb8AQC6LDQhSv0BpiMAPcMk/gJcTzheC2T8offHdEybjP5gu2dQbi+k/CODAyyPw7z+4SFThlSrzP3AhyNwZXfY/KPo72J2P+T/c0q/TIcL8P5SrI8+l9P8/JsJL5ZSTAUCArgXj1iwDQNyav+AYxgRAOId53lpfBkCUczPcnPgHQPBf7dnekQlASEyn1yArC0CkOGHVYsQMQAAlG9OkXQ5AXBHV0Ob2D0DcfkdnFMgQQAp1JGa1lBFANmsBZVZhEkBkYd5j9y0TQA==","dtype":"float64","shape":[50]},"right":{"__ndarray__":"LMePZTgwE8D/0LJml2MSwNHa1Wf2lhHAo+T4aFXKEMDr3DfUaPsPwJDwfdYmYg7ANATE2OTIDMDZFwrboi8LwH4rUN1glgnAIj+W3x79B8DHUtzh3GMGwGxmIuSaygTAEHpo5lgxA8C1ja7oFpgBwLJC6dWp/f+//Gl12iXL/L9GkQHfoZj5v464jeMdZva/2N8Z6Jkz878gB6bsFQHwv9hcZOIjnem/aKt86xs447/w8ynpJ6bZv0AitfYvuMm/AEAuiw0IUr9AaYjAD3DJP4CXE84Xgtk/KH3x3RMm4z+YLtnUG4vpPwjgwMsj8O8/uEhU4ZUq8z9wIcjcGV32Pyj6O9idj/k/3NKv0yHC/D+UqyPPpfT/PybCS+WUkwFAgK4F49YsA0Dcmr/gGMYEQDiHed5aXwZAlHMz3Jz4B0DwX+3Z3pEJQEhMp9cgKwtApDhh1WLEDEAAJRvTpF0OQFwR1dDm9g9A3H5HZxTIEEAKdSRmtZQRQDZrAWVWYRJAZGHeY/ctE0CSV7timPoTQA==","dtype":"float64","shape":[50]},"top":{"__ndarray__":"sg2vfGMOWz/mF2qwz2VQP8PriZgnUVU/vNWZjNPGZz9A/bpzpOZ8P8yHlJDv9IY/7rexaoeTkT9Cr7V3wBScP5HuBxpyAqU/QTHUWLjZqz/eQgmV972yP3r9+yoYHLg/47Ox/kjwvT/iNlKMruPCP1upO2cGlsU/ehSrOYu7xj/l2pVR4mXIP8OmfGzOcsk/90UFJGeLyT8pZS63uT7HP7nzA9+AocU/DfNEGuhPwz/R2JUbQ5S+P88wFZQfiLk/OHpfwO6zsz/aciIOzQ2uPwPpCxfdn6U/FezKT5uGoD/f542Nq/ygP/wrGQ2XrKc/ZScdhg7RtT+02RfIsMLDP2oxk9/KZ88/xAc1TeYt1T+lVDqu+hbZP+h9W6ynptg/ZAZ2DEFV1T9UIOARc+7OPwBlbzCnsMM/1G2oeR8WtT/61dpDR/yiPzYLMfsYXYs/wTmPlAsjZj/RF2qwz2VAP7W/qYB/PEo/tb+pgH88Oj/Ns3SolwlCP/eHlJDv9EY/uiOfiLeYSD/Ns3SolwlCPw==","dtype":"float64","shape":[50]}}},"id":"4d299d7a-88f2-4aed-87f2-90481e3c0367","type":"ColumnDataSource"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"370fe0ce-1ff6-4dc4-a610-5c4e4e7204e9","type":"BoxAnnotation"},{"attributes":{"plot":{"id":"5e8774d8-6ca4-43bd-ad11-257bab2ace33","subtype":"Figure","type":"Plot"}},"id":"6f9cd655-3884-4e33-8b77-1f0b4fe8e46d","type":"WheelZoomTool"},{"attributes":{"plot":null,"text":"sample"},"id":"f38abf79-a824-4973-879c-7d0fa95ccaf9","type":"Title"},{"attributes":{"dimension":1,"plot":{"id":"5e8774d8-6ca4-43bd-ad11-257bab2ace33","subtype":"Figure","type":"Plot"},"ticker":{"id":"9c5db322-3d2b-4fb8-b3fa-25c854978cb7","type":"BasicTicker"}},"id":"a82b6743-dfcf-4c14-8c24-cc1dd58c4f9d","type":"Grid"},{"attributes":{"line_color":{"value":"#ee8822"},"line_width":{"value":2},"x":{"field":"x"},"y":{"field":"y"}},"id":"81ecc2ee-c7a2-41cf-b29d-bddf6505ba74","type":"Line"},{"attributes":{"formatter":{"id":"9a2e26da-4770-4081-a45e-8fe6ff18b054","type":"BasicTickFormatter"},"plot":{"id":"5e8774d8-6ca4-43bd-ad11-257bab2ace33","subtype":"Figure","type":"Plot"},"ticker":{"id":"5b66a4e3-4f26-4167-8bf5-ce97e7e2d424","type":"BasicTicker"}},"id":"bab60c59-2b51-4a94-a965-39898102a646","type":"LinearAxis"},{"attributes":{"callback":null},"id":"09fe5b22-f3a8-4c99-b7e0-2a89fd03553a","type":"DataRange1d"},{"attributes":{"plot":{"id":"5e8774d8-6ca4-43bd-ad11-257bab2ace33","subtype":"Figure","type":"Plot"}},"id":"5bd277f9-b9f6-4c16-b7b6-f174a560748e","type":"HelpTool"},{"attributes":{"callback":null,"column_names":["y","x"],"data":{"x":{"__ndarray__":"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","dtype":"float64","shape":[200]},"y":{"__ndarray__":"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","dtype":"float64","shape":[200]}}},"id":"283fd183-32b0-4a17-8d79-7dd0ea511427","type":"ColumnDataSource"},{"attributes":{},"id":"dcf390ea-7d65-44f9-aad5-8a89f6dcecd1","type":"ToolEvents"},{"attributes":{"plot":{"id":"5e8774d8-6ca4-43bd-ad11-257bab2ace33","subtype":"Figure","type":"Plot"}},"id":"7612835a-fdae-4e04-9909-b7574b2b8c06","type":"SaveTool"},{"attributes":{"plot":{"id":"5e8774d8-6ca4-43bd-ad11-257bab2ace33","subtype":"Figure","type":"Plot"}},"id":"19933866-3b89-4e2a-b71d-7b46ddcde377","type":"ResetTool"},{"attributes":{},"id":"9c5db322-3d2b-4fb8-b3fa-25c854978cb7","type":"BasicTicker"},{"attributes":{"callback":null},"id":"b9498fc0-095b-4184-be7d-6275b6d70740","type":"DataRange1d"},{"attributes":{"active_drag":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"58cb8353-accb-4c7b-8544-1db99e7e2e15","type":"PanTool"},{"id":"6f9cd655-3884-4e33-8b77-1f0b4fe8e46d","type":"WheelZoomTool"},{"id":"23478684-6817-4617-aed5-eae83e6e66fc","type":"BoxZoomTool"},{"id":"7612835a-fdae-4e04-9909-b7574b2b8c06","type":"SaveTool"},{"id":"19933866-3b89-4e2a-b71d-7b46ddcde377","type":"ResetTool"},{"id":"5bd277f9-b9f6-4c16-b7b6-f174a560748e","type":"HelpTool"}]},"id":"4c7b36fa-acde-481c-b791-c8b972a6b9ed","type":"Toolbar"},{"attributes":{},"id":"5b66a4e3-4f26-4167-8bf5-ce97e7e2d424","type":"BasicTicker"},{"attributes":{"overlay":{"id":"370fe0ce-1ff6-4dc4-a610-5c4e4e7204e9","type":"BoxAnnotation"},"plot":{"id":"5e8774d8-6ca4-43bd-ad11-257bab2ace33","subtype":"Figure","type":"Plot"}},"id":"23478684-6817-4617-aed5-eae83e6e66fc","type":"BoxZoomTool"},{"attributes":{},"id":"9a2e26da-4770-4081-a45e-8fe6ff18b054","type":"BasicTickFormatter"},{"attributes":{"bottom":{"value":0},"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"left":{"field":"left"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"right":{"field":"right"},"top":{"field":"top"}},"id":"de2479de-529b-4488-b9fd-ad6e63727335","type":"Quad"},{"attributes":{"data_source":{"id":"4d299d7a-88f2-4aed-87f2-90481e3c0367","type":"ColumnDataSource"},"glyph":{"id":"af9a39d3-07a8-4ee8-b03f-7e61cf59fc07","type":"Quad"},"hover_glyph":null,"nonselection_glyph":{"id":"de2479de-529b-4488-b9fd-ad6e63727335","type":"Quad"},"selection_glyph":null},"id":"092bf1d4-0120-4f98-b6e3-c2f29922161c","type":"GlyphRenderer"},{"attributes":{},"id":"73d40397-a7a4-4e1e-a93d-b55a98053635","type":"BasicTickFormatter"},{"attributes":{"below":[{"id":"bab60c59-2b51-4a94-a965-39898102a646","type":"LinearAxis"}],"left":[{"id":"51abae62-c7d6-4d77-9650-fed60c3e54a9","type":"LinearAxis"}],"plot_height":400,"renderers":[{"id":"bab60c59-2b51-4a94-a965-39898102a646","type":"LinearAxis"},{"id":"ade14e19-86c1-4917-a358-bccaa8d95a82","type":"Grid"},{"id":"51abae62-c7d6-4d77-9650-fed60c3e54a9","type":"LinearAxis"},{"id":"a82b6743-dfcf-4c14-8c24-cc1dd58c4f9d","type":"Grid"},{"id":"370fe0ce-1ff6-4dc4-a610-5c4e4e7204e9","type":"BoxAnnotation"},{"id":"092bf1d4-0120-4f98-b6e3-c2f29922161c","type":"GlyphRenderer"},{"id":"86ee8c6e-9d22-4b0e-9f3c-eda7c8c7ed27","type":"GlyphRenderer"}],"title":{"id":"f38abf79-a824-4973-879c-7d0fa95ccaf9","type":"Title"},"tool_events":{"id":"dcf390ea-7d65-44f9-aad5-8a89f6dcecd1","type":"ToolEvents"},"toolbar":{"id":"4c7b36fa-acde-481c-b791-c8b972a6b9ed","type":"Toolbar"},"x_range":{"id":"09fe5b22-f3a8-4c99-b7e0-2a89fd03553a","type":"DataRange1d"},"y_range":{"id":"b9498fc0-095b-4184-be7d-6275b6d70740","type":"DataRange1d"}},"id":"5e8774d8-6ca4-43bd-ad11-257bab2ace33","subtype":"Figure","type":"Plot"},{"attributes":{"plot":{"id":"5e8774d8-6ca4-43bd-ad11-257bab2ace33","subtype":"Figure","type":"Plot"}},"id":"58cb8353-accb-4c7b-8544-1db99e7e2e15","type":"PanTool"},{"attributes":{"bottom":{"value":0},"fill_color":{"value":"#036564"},"left":{"field":"left"},"line_color":{"value":"#033649"},"right":{"field":"right"},"top":{"field":"top"}},"id":"af9a39d3-07a8-4ee8-b03f-7e61cf59fc07","type":"Quad"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"line_width":{"value":2},"x":{"field":"x"},"y":{"field":"y"}},"id":"5d0b5ddb-3e5a-467f-b469-813c268142e5","type":"Line"},{"attributes":{"data_source":{"id":"283fd183-32b0-4a17-8d79-7dd0ea511427","type":"ColumnDataSource"},"glyph":{"id":"81ecc2ee-c7a2-41cf-b29d-bddf6505ba74","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"5d0b5ddb-3e5a-467f-b469-813c268142e5","type":"Line"},"selection_glyph":null},"id":"86ee8c6e-9d22-4b0e-9f3c-eda7c8c7ed27","type":"GlyphRenderer"},{"attributes":{"plot":{"id":"5e8774d8-6ca4-43bd-ad11-257bab2ace33","subtype":"Figure","type":"Plot"},"ticker":{"id":"5b66a4e3-4f26-4167-8bf5-ce97e7e2d424","type":"BasicTicker"}},"id":"ade14e19-86c1-4917-a358-bccaa8d95a82","type":"Grid"}],"root_ids":["5e8774d8-6ca4-43bd-ad11-257bab2ace33"]},"title":"Bokeh Application","version":"0.12.4"}};
                var render_items = [{"docid":"0f3b9193-dd48-49ee-b76e-fa3f2694fa39","elementid":"838fb569-164e-4414-a2f1-f2516169e1b3","modelid":"5e8774d8-6ca4-43bd-ad11-257bab2ace33"}];
                
                Bokeh.embed.embed_items(docs_json, render_items);
              };
              if (document.readyState != "loading") fn();
              else document.addEventListener("DOMContentLoaded", fn);
            })();
          },
          function(Bokeh) {
          }
        ];
      
        function run_inline_js() {
          
          if ((window.Bokeh !== undefined) || (force === true)) {
            for (var i = 0; i < inline_js.length; i++) {
              inline_js[i](window.Bokeh);
            }if (force === true) {
              display_loaded();
            }} else if (Date.now() < window._bokeh_timeout) {
            setTimeout(run_inline_js, 100);
          } else if (!window._bokeh_failed_load) {
            console.log("Bokeh: BokehJS failed to load within specified timeout.");
            window._bokeh_failed_load = true;
          } else if (force !== true) {
            var cell = $(document.getElementById("838fb569-164e-4414-a2f1-f2516169e1b3")).parents('.cell').data().cell;
            cell.output_area.append_execute_result(NB_LOAD_WARNING)
          }
      
        }
      
        if (window._bokeh_is_loading === 0) {
          console.log("Bokeh: BokehJS loaded, going straight to plotting");
          run_inline_js();
        } else {
          load_libs(js_urls, function() {
            console.log("Bokeh: BokehJS plotting callback run at", now());
            run_inline_js();
          });
        }
      }(this));
    </script>


This method can be quite precise, though at the tails of the
distribution the error gets bigger.

.. code:: ipython3

    dp = (p[1:] - p[:-1]) / (F[1:] - F[:-1])
    x = (F[1:] + F[:-1]) / 2.
    
    fig1 = figure(plot_width=600, plot_height=200, title='check PDF')
    fig1.line(x, pdf(x), line_width=4)
    fig1.line(x, dp, line_width=1.5, color='white')
    
    fig2 = figure(plot_width=600, plot_height=400, title='error', y_axis_type="log")
    fig2.line(x, abs(pdf(x) - dp), line_width=1, color='firebrick')
    
    show(gridplot([[fig1],[fig2]]))



.. raw:: html

    
    
        <div class="bk-root">
            <div class="bk-plotdiv" id="ed25feea-9d36-4454-baa5-4f81d5ea9e09"></div>
        </div>
    <script type="text/javascript">
      
      (function(global) {
        function now() {
          return new Date();
        }
      
        var force = false;
      
        if (typeof (window._bokeh_onload_callbacks) === "undefined" || force === true) {
          window._bokeh_onload_callbacks = [];
          window._bokeh_is_loading = undefined;
        }
      
      
        
        if (typeof (window._bokeh_timeout) === "undefined" || force === true) {
          window._bokeh_timeout = Date.now() + 0;
          window._bokeh_failed_load = false;
        }
      
        var NB_LOAD_WARNING = {'data': {'text/html':
           "<div style='background-color: #fdd'>\n"+
           "<p>\n"+
           "BokehJS does not appear to have successfully loaded. If loading BokehJS from CDN, this \n"+
           "may be due to a slow or bad network connection. Possible fixes:\n"+
           "</p>\n"+
           "<ul>\n"+
           "<li>re-rerun `output_notebook()` to attempt to load from CDN again, or</li>\n"+
           "<li>use INLINE resources instead, as so:</li>\n"+
           "</ul>\n"+
           "<code>\n"+
           "from bokeh.resources import INLINE\n"+
           "output_notebook(resources=INLINE)\n"+
           "</code>\n"+
           "</div>"}};
      
        function display_loaded() {
          if (window.Bokeh !== undefined) {
            document.getElementById("ed25feea-9d36-4454-baa5-4f81d5ea9e09").textContent = "BokehJS successfully loaded.";
          } else if (Date.now() < window._bokeh_timeout) {
            setTimeout(display_loaded, 100)
          }
        }
      
        function run_callbacks() {
          window._bokeh_onload_callbacks.forEach(function(callback) { callback() });
          delete window._bokeh_onload_callbacks
          console.info("Bokeh: all callbacks have finished");
        }
      
        function load_libs(js_urls, callback) {
          window._bokeh_onload_callbacks.push(callback);
          if (window._bokeh_is_loading > 0) {
            console.log("Bokeh: BokehJS is being loaded, scheduling callback at", now());
            return null;
          }
          if (js_urls == null || js_urls.length === 0) {
            run_callbacks();
            return null;
          }
          console.log("Bokeh: BokehJS not loaded, scheduling load and callback at", now());
          window._bokeh_is_loading = js_urls.length;
          for (var i = 0; i < js_urls.length; i++) {
            var url = js_urls[i];
            var s = document.createElement('script');
            s.src = url;
            s.async = false;
            s.onreadystatechange = s.onload = function() {
              window._bokeh_is_loading--;
              if (window._bokeh_is_loading === 0) {
                console.log("Bokeh: all BokehJS libraries loaded");
                run_callbacks()
              }
            };
            s.onerror = function() {
              console.warn("failed to load library " + url);
            };
            console.log("Bokeh: injecting script tag for BokehJS library: ", url);
            document.getElementsByTagName("head")[0].appendChild(s);
          }
        };var element = document.getElementById("ed25feea-9d36-4454-baa5-4f81d5ea9e09");
        if (element == null) {
          console.log("Bokeh: ERROR: autoload.js configured with elementid 'ed25feea-9d36-4454-baa5-4f81d5ea9e09' but no matching script tag was found. ")
          return false;
        }
      
        var js_urls = [];
      
        var inline_js = [
          function(Bokeh) {
            (function() {
              var fn = function() {
                var docs_json = {"44fdea8b-16b9-413e-867e-f5b471747404":{"roots":{"references":[{"attributes":{"plot":null,"text":"error"},"id":"6d102dbe-58d1-49c5-a9e2-c018e8334940","type":"Title"},{"attributes":{"callback":null,"column_names":["y","x"],"data":{"x":{"__ndarray__":"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","dtype":"float32","shape":[1024]},"y":{"__ndarray__":"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","dtype":"float64","shape":[1024]}}},"id":"a17ec941-24bc-495d-abc3-36dfc0ce8b6f","type":"ColumnDataSource"},{"attributes":{"plot":{"id":"89c489ce-e1a3-423b-ac89-47b252c94d79","subtype":"Figure","type":"Plot"},"ticker":{"id":"4d1b7273-154c-4957-ae0d-e41b0dfc50a7","type":"BasicTicker"}},"id":"5e452bb0-a939-4cdb-87e8-f38e9674edf7","type":"Grid"},{"attributes":{},"id":"9062a07c-cbd3-4cf5-bd57-aa224eabfd5d","type":"BasicTickFormatter"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"line_width":{"value":4},"x":{"field":"x"},"y":{"field":"y"}},"id":"23a15b12-6b75-4994-814c-0cc6600fabf0","type":"Line"},{"attributes":{},"id":"177c92cb-90c0-400a-9156-fc6aff1d93a5","type":"BasicTickFormatter"},{"attributes":{"formatter":{"id":"177c92cb-90c0-400a-9156-fc6aff1d93a5","type":"BasicTickFormatter"},"plot":{"id":"22054ba4-7480-45c1-b316-b854034d40df","subtype":"Figure","type":"Plot"},"ticker":{"id":"ab159471-62b8-4f05-a1ed-375727479c2a","type":"BasicTicker"}},"id":"d6748532-6a4f-455f-b2bd-e28ad72fd9ea","type":"LinearAxis"},{"attributes":{"data_source":{"id":"a17ec941-24bc-495d-abc3-36dfc0ce8b6f","type":"ColumnDataSource"},"glyph":{"id":"b4181707-ec1e-498b-858b-ea9a5bd8691d","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"5a0bfde5-3798-47d5-896d-dc8081d40c14","type":"Line"},"selection_glyph":null},"id":"4b66a7c4-bf92-44d8-a3ca-7f53a9527001","type":"GlyphRenderer"},{"attributes":{"callback":null,"column_names":["y","x"],"data":{"x":{"__ndarray__":"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","dtype":"float32","shape":[1024]},"y":{"__ndarray__":"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","dtype":"float32","shape":[1024]}}},"id":"75089f23-cfad-4c68-a676-80a57281853d","type":"ColumnDataSource"},{"attributes":{"ticker":null},"id":"44a36728-1f52-4ea9-aa28-29bc96e96225","type":"LogTickFormatter"},{"attributes":{},"id":"14eb9e2e-545d-406e-81b0-8a3abc9683f2","type":"ToolEvents"},{"attributes":{},"id":"8ca33a41-c84e-4b7b-9d1f-952ddb8edad7","type":"BasicTicker"},{"attributes":{"plot":{"id":"22054ba4-7480-45c1-b316-b854034d40df","subtype":"Figure","type":"Plot"}},"id":"4f42cae9-95bd-4873-be3c-d3decb8a4ded","type":"HelpTool"},{"attributes":{},"id":"3349a80f-f50a-48aa-a2db-25bab575a29d","type":"BasicTickFormatter"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"line_width":{"value":1.5},"x":{"field":"x"},"y":{"field":"y"}},"id":"510994fe-eacc-4587-90c2-711f63d1d438","type":"Line"},{"attributes":{"callback":null},"id":"a629f80a-441c-4dc2-92c6-ec5475fcf180","type":"DataRange1d"},{"attributes":{"formatter":{"id":"9062a07c-cbd3-4cf5-bd57-aa224eabfd5d","type":"BasicTickFormatter"},"plot":{"id":"89c489ce-e1a3-423b-ac89-47b252c94d79","subtype":"Figure","type":"Plot"},"ticker":{"id":"4d1b7273-154c-4957-ae0d-e41b0dfc50a7","type":"BasicTicker"}},"id":"2a37cb48-fe5d-4c1e-9603-03fc182c13a7","type":"LinearAxis"},{"attributes":{"callback":null},"id":"3ae80170-bfda-4cdf-8d2a-c47b1160497d","type":"DataRange1d"},{"attributes":{"plot":{"id":"22054ba4-7480-45c1-b316-b854034d40df","subtype":"Figure","type":"Plot"}},"id":"5c2820fe-45d2-43a4-b641-73f36c4544be","type":"ResetTool"},{"attributes":{"active_drag":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"bd2f27aa-21c3-473d-acbb-978acad621f8","type":"PanTool"},{"id":"7f2ab2be-eaff-4b11-b595-f1fb29d9913c","type":"WheelZoomTool"},{"id":"544f64cb-dac8-4467-920c-17a0e739e04b","type":"BoxZoomTool"},{"id":"029e685f-fd27-4d96-aa6d-23376add7251","type":"SaveTool"},{"id":"7420235d-2423-46b4-bf42-44f27dc085f1","type":"ResetTool"},{"id":"ef8b097b-367e-430c-8c96-6f49c1e0935c","type":"HelpTool"}]},"id":"b3f3b528-0095-4362-8622-7be743687e63","type":"Toolbar"},{"attributes":{"callback":null},"id":"18f4756c-1355-457e-8bc0-003007f231b6","type":"DataRange1d"},{"attributes":{"plot":{"id":"89c489ce-e1a3-423b-ac89-47b252c94d79","subtype":"Figure","type":"Plot"}},"id":"ef8b097b-367e-430c-8c96-6f49c1e0935c","type":"HelpTool"},{"attributes":{"formatter":{"id":"3349a80f-f50a-48aa-a2db-25bab575a29d","type":"BasicTickFormatter"},"plot":{"id":"22054ba4-7480-45c1-b316-b854034d40df","subtype":"Figure","type":"Plot"},"ticker":{"id":"8ca33a41-c84e-4b7b-9d1f-952ddb8edad7","type":"BasicTicker"}},"id":"97cfe190-84b0-4c17-90d2-107378b96d61","type":"LinearAxis"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"421710e3-5b13-476a-924f-e0f9e480c197","type":"BoxAnnotation"},{"attributes":{"line_color":{"value":"white"},"line_width":{"value":1.5},"x":{"field":"x"},"y":{"field":"y"}},"id":"3a85141c-46ff-4085-a733-164e021dd403","type":"Line"},{"attributes":{"overlay":{"id":"bf22642c-f45c-4792-803d-3debc7bc1fea","type":"BoxAnnotation"},"plot":{"id":"22054ba4-7480-45c1-b316-b854034d40df","subtype":"Figure","type":"Plot"}},"id":"2499a076-91df-41a3-ad83-51de8b5d0159","type":"BoxZoomTool"},{"attributes":{"num_minor_ticks":10},"id":"ad741e22-0700-43a3-9185-e9b20376d708","type":"LogTicker"},{"attributes":{"plot":{"id":"89c489ce-e1a3-423b-ac89-47b252c94d79","subtype":"Figure","type":"Plot"}},"id":"029e685f-fd27-4d96-aa6d-23376add7251","type":"SaveTool"},{"attributes":{"below":[{"id":"2a37cb48-fe5d-4c1e-9603-03fc182c13a7","type":"LinearAxis"}],"left":[{"id":"6ebf6e45-235f-4d1e-bbe4-a8dcb0c1b6ad","type":"LogAxis"}],"plot_height":400,"renderers":[{"id":"2a37cb48-fe5d-4c1e-9603-03fc182c13a7","type":"LinearAxis"},{"id":"5e452bb0-a939-4cdb-87e8-f38e9674edf7","type":"Grid"},{"id":"6ebf6e45-235f-4d1e-bbe4-a8dcb0c1b6ad","type":"LogAxis"},{"id":"3f61a5c0-9759-414e-bb16-e1b64654ca7d","type":"Grid"},{"id":"421710e3-5b13-476a-924f-e0f9e480c197","type":"BoxAnnotation"},{"id":"4b66a7c4-bf92-44d8-a3ca-7f53a9527001","type":"GlyphRenderer"}],"title":{"id":"6d102dbe-58d1-49c5-a9e2-c018e8334940","type":"Title"},"tool_events":{"id":"d9cbbe76-844a-4b89-965c-3b817e378a84","type":"ToolEvents"},"toolbar":{"id":"b3f3b528-0095-4362-8622-7be743687e63","type":"Toolbar"},"toolbar_location":null,"x_range":{"id":"3ae80170-bfda-4cdf-8d2a-c47b1160497d","type":"DataRange1d"},"y_mapper_type":"log","y_range":{"id":"a629f80a-441c-4dc2-92c6-ec5475fcf180","type":"DataRange1d"}},"id":"89c489ce-e1a3-423b-ac89-47b252c94d79","subtype":"Figure","type":"Plot"},{"attributes":{"overlay":{"id":"421710e3-5b13-476a-924f-e0f9e480c197","type":"BoxAnnotation"},"plot":{"id":"89c489ce-e1a3-423b-ac89-47b252c94d79","subtype":"Figure","type":"Plot"}},"id":"544f64cb-dac8-4467-920c-17a0e739e04b","type":"BoxZoomTool"},{"attributes":{},"id":"ab159471-62b8-4f05-a1ed-375727479c2a","type":"BasicTicker"},{"attributes":{"children":[{"id":"89c489ce-e1a3-423b-ac89-47b252c94d79","subtype":"Figure","type":"Plot"}]},"id":"6d7c5d0f-1e6f-4de3-8547-564b2f687b0d","type":"Row"},{"attributes":{"children":[{"id":"22054ba4-7480-45c1-b316-b854034d40df","subtype":"Figure","type":"Plot"}]},"id":"25bda856-7dc2-45e1-9d4b-e81cf08ab4ee","type":"Row"},{"attributes":{"plot":{"id":"89c489ce-e1a3-423b-ac89-47b252c94d79","subtype":"Figure","type":"Plot"}},"id":"bd2f27aa-21c3-473d-acbb-978acad621f8","type":"PanTool"},{"attributes":{"formatter":{"id":"44a36728-1f52-4ea9-aa28-29bc96e96225","type":"LogTickFormatter"},"plot":{"id":"89c489ce-e1a3-423b-ac89-47b252c94d79","subtype":"Figure","type":"Plot"},"ticker":{"id":"ad741e22-0700-43a3-9185-e9b20376d708","type":"LogTicker"}},"id":"6ebf6e45-235f-4d1e-bbe4-a8dcb0c1b6ad","type":"LogAxis"},{"attributes":{"plot":{"id":"22054ba4-7480-45c1-b316-b854034d40df","subtype":"Figure","type":"Plot"},"ticker":{"id":"8ca33a41-c84e-4b7b-9d1f-952ddb8edad7","type":"BasicTicker"}},"id":"9561b3ee-719e-42fb-900d-a9d689550c10","type":"Grid"},{"attributes":{"plot":{"id":"22054ba4-7480-45c1-b316-b854034d40df","subtype":"Figure","type":"Plot"}},"id":"9aa4817b-4aeb-4514-8991-3bbb5f04200a","type":"PanTool"},{"attributes":{"below":[{"id":"97cfe190-84b0-4c17-90d2-107378b96d61","type":"LinearAxis"}],"left":[{"id":"d6748532-6a4f-455f-b2bd-e28ad72fd9ea","type":"LinearAxis"}],"plot_height":200,"renderers":[{"id":"97cfe190-84b0-4c17-90d2-107378b96d61","type":"LinearAxis"},{"id":"9561b3ee-719e-42fb-900d-a9d689550c10","type":"Grid"},{"id":"d6748532-6a4f-455f-b2bd-e28ad72fd9ea","type":"LinearAxis"},{"id":"61243bfb-e705-4d6a-b510-1be7a3359cf1","type":"Grid"},{"id":"bf22642c-f45c-4792-803d-3debc7bc1fea","type":"BoxAnnotation"},{"id":"625e6c1a-49ed-4403-a03c-d51868a1bef5","type":"GlyphRenderer"},{"id":"b7d99500-4baf-425e-bf2d-785357ae5c83","type":"GlyphRenderer"}],"title":{"id":"1ede6b48-ff52-46d7-b6de-6774752d73b6","type":"Title"},"tool_events":{"id":"14eb9e2e-545d-406e-81b0-8a3abc9683f2","type":"ToolEvents"},"toolbar":{"id":"1f186e21-2d31-44ed-b5bc-4a7713c887b4","type":"Toolbar"},"toolbar_location":null,"x_range":{"id":"06b95d62-6b1f-4244-a2f8-45ce9d18493a","type":"DataRange1d"},"y_range":{"id":"18f4756c-1355-457e-8bc0-003007f231b6","type":"DataRange1d"}},"id":"22054ba4-7480-45c1-b316-b854034d40df","subtype":"Figure","type":"Plot"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"5a0bfde5-3798-47d5-896d-dc8081d40c14","type":"Line"},{"attributes":{"children":[{"id":"25bda856-7dc2-45e1-9d4b-e81cf08ab4ee","type":"Row"},{"id":"6d7c5d0f-1e6f-4de3-8547-564b2f687b0d","type":"Row"}]},"id":"7e67f48c-7953-4448-ba27-5e5c8913ca84","type":"Column"},{"attributes":{"plot":null,"text":"check PDF"},"id":"1ede6b48-ff52-46d7-b6de-6774752d73b6","type":"Title"},{"attributes":{"callback":null,"column_names":["y","x"],"data":{"x":{"__ndarray__":"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","dtype":"float32","shape":[1024]},"y":{"__ndarray__":"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","dtype":"float64","shape":[1024]}}},"id":"e53b322c-7f77-4ebe-b629-0826663964ce","type":"ColumnDataSource"},{"attributes":{"dimension":1,"plot":{"id":"89c489ce-e1a3-423b-ac89-47b252c94d79","subtype":"Figure","type":"Plot"},"ticker":{"id":"ad741e22-0700-43a3-9185-e9b20376d708","type":"LogTicker"}},"id":"3f61a5c0-9759-414e-bb16-e1b64654ca7d","type":"Grid"},{"attributes":{"data_source":{"id":"75089f23-cfad-4c68-a676-80a57281853d","type":"ColumnDataSource"},"glyph":{"id":"901a9cac-2002-4463-a73a-e870140f8ec4","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"23a15b12-6b75-4994-814c-0cc6600fabf0","type":"Line"},"selection_glyph":null},"id":"625e6c1a-49ed-4403-a03c-d51868a1bef5","type":"GlyphRenderer"},{"attributes":{"line_color":{"value":"firebrick"},"x":{"field":"x"},"y":{"field":"y"}},"id":"b4181707-ec1e-498b-858b-ea9a5bd8691d","type":"Line"},{"attributes":{"dimension":1,"plot":{"id":"22054ba4-7480-45c1-b316-b854034d40df","subtype":"Figure","type":"Plot"},"ticker":{"id":"ab159471-62b8-4f05-a1ed-375727479c2a","type":"BasicTicker"}},"id":"61243bfb-e705-4d6a-b510-1be7a3359cf1","type":"Grid"},{"attributes":{},"id":"4d1b7273-154c-4957-ae0d-e41b0dfc50a7","type":"BasicTicker"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"bf22642c-f45c-4792-803d-3debc7bc1fea","type":"BoxAnnotation"},{"attributes":{"callback":null},"id":"06b95d62-6b1f-4244-a2f8-45ce9d18493a","type":"DataRange1d"},{"attributes":{"plot":{"id":"89c489ce-e1a3-423b-ac89-47b252c94d79","subtype":"Figure","type":"Plot"}},"id":"7f2ab2be-eaff-4b11-b595-f1fb29d9913c","type":"WheelZoomTool"},{"attributes":{"data_source":{"id":"e53b322c-7f77-4ebe-b629-0826663964ce","type":"ColumnDataSource"},"glyph":{"id":"3a85141c-46ff-4085-a733-164e021dd403","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"510994fe-eacc-4587-90c2-711f63d1d438","type":"Line"},"selection_glyph":null},"id":"b7d99500-4baf-425e-bf2d-785357ae5c83","type":"GlyphRenderer"},{"attributes":{"children":[{"id":"6bf647c1-5cfa-4d13-a424-48cfbec3353e","type":"ToolbarBox"},{"id":"7e67f48c-7953-4448-ba27-5e5c8913ca84","type":"Column"}]},"id":"623ec4b9-63be-4a74-a750-43861b70a621","type":"Column"},{"attributes":{"plot":{"id":"22054ba4-7480-45c1-b316-b854034d40df","subtype":"Figure","type":"Plot"}},"id":"65cf3b91-1aba-467e-a883-130fe93b5478","type":"SaveTool"},{"attributes":{},"id":"d9cbbe76-844a-4b89-965c-3b817e378a84","type":"ToolEvents"},{"attributes":{"sizing_mode":"scale_width","toolbar_location":"above","tools":[{"id":"9aa4817b-4aeb-4514-8991-3bbb5f04200a","type":"PanTool"},{"id":"cfbd0efe-2230-4b9b-bfde-af6e40032044","type":"WheelZoomTool"},{"id":"2499a076-91df-41a3-ad83-51de8b5d0159","type":"BoxZoomTool"},{"id":"65cf3b91-1aba-467e-a883-130fe93b5478","type":"SaveTool"},{"id":"5c2820fe-45d2-43a4-b641-73f36c4544be","type":"ResetTool"},{"id":"4f42cae9-95bd-4873-be3c-d3decb8a4ded","type":"HelpTool"},{"id":"bd2f27aa-21c3-473d-acbb-978acad621f8","type":"PanTool"},{"id":"7f2ab2be-eaff-4b11-b595-f1fb29d9913c","type":"WheelZoomTool"},{"id":"544f64cb-dac8-4467-920c-17a0e739e04b","type":"BoxZoomTool"},{"id":"029e685f-fd27-4d96-aa6d-23376add7251","type":"SaveTool"},{"id":"7420235d-2423-46b4-bf42-44f27dc085f1","type":"ResetTool"},{"id":"ef8b097b-367e-430c-8c96-6f49c1e0935c","type":"HelpTool"}]},"id":"6bf647c1-5cfa-4d13-a424-48cfbec3353e","type":"ToolbarBox"},{"attributes":{"plot":{"id":"89c489ce-e1a3-423b-ac89-47b252c94d79","subtype":"Figure","type":"Plot"}},"id":"7420235d-2423-46b4-bf42-44f27dc085f1","type":"ResetTool"},{"attributes":{"plot":{"id":"22054ba4-7480-45c1-b316-b854034d40df","subtype":"Figure","type":"Plot"}},"id":"cfbd0efe-2230-4b9b-bfde-af6e40032044","type":"WheelZoomTool"},{"attributes":{"line_color":{"value":"#1f77b4"},"line_width":{"value":4},"x":{"field":"x"},"y":{"field":"y"}},"id":"901a9cac-2002-4463-a73a-e870140f8ec4","type":"Line"},{"attributes":{"active_drag":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"9aa4817b-4aeb-4514-8991-3bbb5f04200a","type":"PanTool"},{"id":"cfbd0efe-2230-4b9b-bfde-af6e40032044","type":"WheelZoomTool"},{"id":"2499a076-91df-41a3-ad83-51de8b5d0159","type":"BoxZoomTool"},{"id":"65cf3b91-1aba-467e-a883-130fe93b5478","type":"SaveTool"},{"id":"5c2820fe-45d2-43a4-b641-73f36c4544be","type":"ResetTool"},{"id":"4f42cae9-95bd-4873-be3c-d3decb8a4ded","type":"HelpTool"}]},"id":"1f186e21-2d31-44ed-b5bc-4a7713c887b4","type":"Toolbar"}],"root_ids":["623ec4b9-63be-4a74-a750-43861b70a621"]},"title":"Bokeh Application","version":"0.12.4"}};
                var render_items = [{"docid":"44fdea8b-16b9-413e-867e-f5b471747404","elementid":"ed25feea-9d36-4454-baa5-4f81d5ea9e09","modelid":"623ec4b9-63be-4a74-a750-43861b70a621"}];
                
                Bokeh.embed.embed_items(docs_json, render_items);
              };
              if (document.readyState != "loading") fn();
              else document.addEventListener("DOMContentLoaded", fn);
            })();
          },
          function(Bokeh) {
          }
        ];
      
        function run_inline_js() {
          
          if ((window.Bokeh !== undefined) || (force === true)) {
            for (var i = 0; i < inline_js.length; i++) {
              inline_js[i](window.Bokeh);
            }if (force === true) {
              display_loaded();
            }} else if (Date.now() < window._bokeh_timeout) {
            setTimeout(run_inline_js, 100);
          } else if (!window._bokeh_failed_load) {
            console.log("Bokeh: BokehJS failed to load within specified timeout.");
            window._bokeh_failed_load = true;
          } else if (force !== true) {
            var cell = $(document.getElementById("ed25feea-9d36-4454-baa5-4f81d5ea9e09")).parents('.cell').data().cell;
            cell.output_area.append_execute_result(NB_LOAD_WARNING)
          }
      
        }
      
        if (window._bokeh_is_loading === 0) {
          console.log("Bokeh: BokehJS loaded, going straight to plotting");
          run_inline_js();
        } else {
          load_libs(js_urls, function() {
            console.log("Bokeh: BokehJS plotting callback run at", now());
            run_inline_js();
          });
        }
      }(this));
    </script>

