def counties_choropleth(assignment, color, fip, name):
    '''Create U.S. counties map and color each county by clutering assignments'''
    import plotly.figure_factory as ff

    fig = ff.create_choropleth(
            fips = fips, values = [str(i+1) for i in assignment], scope=['usa'],
        colorscale = color,
        title = 'Three clusters among U.S. counties based on {}'.format(name))

    fig.show()
    return fig