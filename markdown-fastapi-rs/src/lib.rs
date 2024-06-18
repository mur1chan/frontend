use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn md_to_html(input: &str) -> PyResult<String> {
    Ok(markdown::to_html(input))
}

/// A Python module implemented in Rust.
#[pymodule]
fn markdown_fastapi_rs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(md_to_html, m)?)?;
    Ok(())
}
