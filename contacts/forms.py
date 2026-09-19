import re
from django import forms
from .models import LicitacionContacto

class LicitacionContactoForm(forms.ModelForm):
    class Meta:
        model = LicitacionContacto
        fields = [
            "nombre_empresa", 
            "cuit", 
            "email", 
            "telefono", 
            "tipo_cliente", 
            "mensaje", 
            "archivo_adjunto"
        ]
        widgets = {
            "nombre_empresa": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-600 focus:border-transparent transition duration-200 bg-white text-slate-800",
                "placeholder": "Ej: Constructora S.A. o Nombre del profesional"
            }),
            "cuit": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-600 focus:border-transparent transition duration-200 bg-white text-slate-800",
                "placeholder": "Ej: 20-30456789-2 o 20304567892"
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full px-4 py-3 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-600 focus:border-transparent transition duration-200 bg-white text-slate-800",
                "placeholder": "Ej: contacto@empresa.com.ar"
            }),
            "telefono": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-600 focus:border-transparent transition duration-200 bg-white text-slate-800",
                "placeholder": "Ej: +54 9 351 1234567"
            }),
            "tipo_cliente": forms.Select(attrs={
                "class": "w-full px-4 py-3 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-600 focus:border-transparent transition duration-200 bg-white text-slate-800",
            }),
            "mensaje": forms.Textarea(attrs={
                "class": "w-full px-4 py-3 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-600 focus:border-transparent transition duration-200 bg-white text-slate-800",
                "rows": 4,
                "placeholder": "Detalla los productos, volúmenes de compra, pliego o detalles del proyecto..."
            }),
            "archivo_adjunto": forms.ClearableFileInput(attrs={
                "class": "w-full text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-sky-50 file:text-sky-700 hover:file:bg-sky-100 transition duration-200 cursor-pointer"
            })
        }

    def clean_cuit(self):
        cuit = self.cleaned_data.get("cuit", "").strip()
        # Eliminar guiones y espacios
        cuit_clean = re.sub(r"[- \s]", "", cuit)
        
        if not cuit_clean.isdigit():
            raise forms.ValidationError("El CUIT solo debe contener números y opcionalmente guiones.")
        
        if len(cuit_clean) != 11:
            raise forms.ValidationError("El CUIT debe tener exactamente 11 números.")
        
        # Opcional: Re-formatear CUIT para almacenamiento uniforme
        return f"{cuit_clean[:2]}-{cuit_clean[2:10]}-{cuit_clean[10]}"
