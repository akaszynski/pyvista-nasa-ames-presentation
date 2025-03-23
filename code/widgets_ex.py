pl = pv.Plotter()
pl.add_mesh(
    starting_mesh,
    show_edges=True,
)
pl.add_slider_widget(
    callback=callback,
    rng=[3, 60],
    value=30,
    title="Phi Resolution",
    pointa=(0.025, 0.1),
    pointb=(0.31, 0.1),
    style="modern",
)
