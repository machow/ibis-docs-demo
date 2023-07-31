# ibis-docs-demo

* [netlify site](https://main--frabjous-dragon-e893db.netlify.app)


## Translating from mkdocs to quarto

### Callouts

In mkdocs callouts use the syntax below.

``````
!!! info I am an informative message
``````

Use [quarto's callout syntax](https://quarto.org/docs/authoring/callouts.html#callout-types) to produce the same effect:


``````
::: {.callout-info}
I am an informative message.
:::
``````


### Tabsets

Use [quarto's tabset syntax](https://quarto.org/docs/output-formats/html-basics.html#tabsets)


``````
::: {.panel-tabset}
## R

``` {.r}
1 + 1
```

## Python

``` {.python}
2 + 2
```

:::
``````

